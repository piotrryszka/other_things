# coord = (33.9422, -118.676374)
# lat, long = coord
# print(long)

city, year, pop, chg, area = ('Warsaw', 2002, 364735, 0.66, 8439)
traveler_ids = [('BRA', '3526362'), ('POL', '2367432'), ('USA', '3232432')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

# b,a = a,b

# l = divmod(20, 8)
# print(l)
# t = (20, 8)
# m = divmod(*t)
# print(m)
# q, r = divmod(*t)
# print(q, r)

# a, b, *reszta = range(2)
# print(a, b, reszta)

# *a, b, c, d = range(5)
# print(a, b, c, d)

adresy = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('miasto', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (lat, long) in adresy:
    if long <= 0:
        print(fmt.format(name, lat, long))
