import functools
import unicodedata
from functools import partial
from operator import mul

triple = partial(mul, 3)
print(triple(7))

print(list(map(triple, range(1, 10))))

nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(s1 == s2)

print(nfc(s1) == nfc(s2))
