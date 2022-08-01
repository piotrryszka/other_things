import array

symbols = '%^&*$¢£¥€¤'

b_ascii = [ord(s) for s in symbols if ord(s) < 127]
# print(b_ascii)

c_ascii = list(filter(lambda c: c < 127, map(ord, symbols)))
# print(c_ascii)

print(tuple(ord(symbol) for symbol in symbols))

print(array.array('I', (ord(symbol) for symbol in symbols)))

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# tshirt = [(color, size) for color in colors for size in sizes]
# print(tshirt)
for tshirt in ('koszulka w kolorze %s jest dostępna w rozmiarze %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# for color in colors:
#     for size in sizes:
#         print((color, size))


