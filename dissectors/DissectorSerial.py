from DissectorBase import DissectorBase

class Dissector(DissectorBase):
	def __init__(self):
		super().__init__()

	def ingest(self, raw: str) -> None:
		for start_bits in [0,1,2]:
			for stop_bits in [0,1,2,3]: # including parity
				for data_bits in [6,7,8,9,10,11]:
					packet_len = start_bits + data_bits + stop_bits
					for pad_bits in range(packet_len):
						modified_inp = self.pad_input(raw, pad_bits, packet_len)
						self.generate_variant(modified_inp, start_bits, data_bits, stop_bits, pad_bits)

	def pad_input(self, inp, pad_bits, packet_length):
		first_char = inp[0]
		last_char = inp[-1]
		inp = first_char * pad_bits + inp
		length = len(inp)
		inp = inp + last_char * (packet_length - length % packet_length)
		return inp

	def generate_variant(self, inp, start, data, stop, pad):
		var_littleEndian = ''
		var_bigEndian = ''
		for ix in range(0, len(inp), (start + data + stop)):
			data_value = inp[ix + start : ix + start + data]
			var_littleEndian += chr(int(data_value[::-1],2))
			var_bigEndian += chr(int(data_value,2))
		self.add_variant(var_littleEndian, f'Serial (LE) ({pad})[{start}][{data}][{stop}]')
		self.add_variant(var_bigEndian, f'Serial (BE) ({pad})[{start}][{data}][{stop}]')
