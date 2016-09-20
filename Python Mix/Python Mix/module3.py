upper = "".join([chr(ascii) for ascii in range(65,91)])
lower = "".join([chr(ascii) for ascii in range(97,123)])
digit = "".join([chr(ascii) for ascii in range(48,58)])

ALPHABET = upper + lower +digit + "'"
KEY = range(len(ALPHABET))
MSG = "AX qgm lZafc UjqhlgYjShZq ak lZW SfkoWj lg qgmj hjgTdWe, lZWf qgm Vgf2l cfgo oZSl qgmj hjgTdWe ak. FWmeSff, usst"

for k in KEY:
    out = ""
    for c in MSG:
        try:
            out += ALPHABET[(ALPHABET.index(c) + k) % len(ALPHABET)]
        except:
            out += c
    print("%d: %s" % (k, out))