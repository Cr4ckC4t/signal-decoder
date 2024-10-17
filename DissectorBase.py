class DissectorBase:
	def __init__(self):
		self._input_vars = {}

	def ingest(self, raw: str) -> None:
		# append possible/valid decoded input variations to self._input_vars using add_variant
		pass

	def add_variant(self, variant: str, name: str) -> None:
		self._input_vars[name] = variant

	def filter(self, needle: str, ignore_case: bool) -> None:
		"""
		Remove all variants that dont contain the needle
		"""
		self._input_vars = { name: variant
		  for name, variant
		  in self._input_vars.items()
		  if (needle in variant) or
		    (ignore_case and
		    ((needle.lower() in variant) or (needle.upper() in variant)))
		}

	def show_variants(self):
		for name,variant in self._input_vars.items():
			print(f'======> {name}:\n {variant}')
