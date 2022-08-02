from collections import namedtuple
from functools import reduce
from operator import mul, itemgetter, attrgetter


def fac(n):
    return reduce(mul, range(1, n + 1))


adresy = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

for city in sorted(adresy, key=itemgetter(1)):
    print(city)

cc = itemgetter(1, 0)
for city in adresy:
    print(cc(city))

LatLong = namedtuple('Latlong', 'lat long')
Miasta = namedtuple('Miasta', 'name cc pop coord')
areas = [Miasta(name, cc, pop, LatLong(lat, long))
         for name, cc, pop, (lat, long) in adresy]
print(areas[0])
print(areas[0].coord.lat)

name_lat = attrgetter('name', 'coord.lat')

for city in sorted(areas, key=attrgetter('coord.lat')):
    print(name_lat(city))
