from os import listdir
from os.path import dirname, isfile, join

__all__ = []

baseDirectory = dirname(__file__)
files = listdir(baseDirectory)
for file in files:
	if isfile(join(baseDirectory,file)) and file.startswith('Dis') and file.endswith('.py'):
		__all__.append(file.strip('.py'))
		
