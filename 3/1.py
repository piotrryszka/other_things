from collections import abc

my = dict()
my2 = {}
my3 = dict(zip([], []))
# my4 = dict([(),()])
my5 = dict({})

codes = [(3451, 'PL'),
         (342, 'CH'),
         (53, 'DE'),
         (214, 'UK'),
         (765, 'NL')]

cc = {country: code for code, country in codes}
cc2 = {code: country.lower() for country, code in cc.items() if code < 342}
print(cc2)
print(cc['de'])
print(cc.get('de'))

