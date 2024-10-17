# Signal Decoder

> Pluggable signal decoder for CTFs.

This was put together during a long night drive in the bus coming home from a CTF (don't expect anything). It aims to solve the problem of having a signal pattern consisting of only 1s and 0s that contains an encoded message. It's written to be extended easily by writing new dissectors (under `dissectors/`). Currently, the only dissector that exists brute forces the most common combinations of serial communication (none or some start bits, some data bits, none or some stop bits - e.g. parity and padding of the message).

Every dissector is supposed to call `add_variant` in the `ingest` method with the decoded value of the input.

After all dissectors had their chance to decode the input and submitted possible results, the `filter` method is used to discard all variants that don't contain a specified string (like `ctf{`).

Finally, `show_variants` prints all results.

---

To add your own dissector, just copy the existing one and modify the logic to interpret the input (the file must start with `Dis` and end with `.py`). Next up could be a dissector for NRZ (and its variants).
