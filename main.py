#!/usr/bin/env python3

import sys
from dissectors import *

def parse_file(fp):
	# expects a file with one line of 1s and 0s
	raw = ''
	try:
		with open(fp, 'r') as f:
			raw = f.read()

		raw = raw.strip('\n')

		if not len(raw):
			print(f'{fp} appears to be empty. Nothing to do.')
			sys.exit(0)

	except Exception as e:
		print(f'[!] Error loading {fp}: {e}')
		sys.exit(1)

	return raw

def enumerate_dissectors():
	dissectors = {}
	pkg = sys.modules['dissectors']
	names = pkg.__all__
	for name in names:
		module = getattr(pkg,name)
		cls = getattr(module,'Dissector')
		dissectors[name] = cls
	return dissectors

def main(inp):
	raw = parse_file(inp)

	dissectors = enumerate_dissectors()

	for name,dissector in dissectors.items():
		try:
			print(f'Trying {name}')
			d = dissector()
			d.ingest(raw)
			d.filter("Auth Key:", ignore_case=True)
			# add other filters if needed
			d.show_variants()

		except Exception as e:
			print(f'Dissector {name} threw an exception: {e}')
			sys.exit(1)

if __name__ == '__main__':
	main(sys.argv[1])
