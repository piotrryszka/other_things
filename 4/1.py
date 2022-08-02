from _operator import add
from functools import reduce


def factorial(n):
    ''' zwraca n '''
    return 1 if n < 2 else n * factorial(n - 1)


# print(factorial(42))
# print(factorial.__doc__)
# print(type(factorial))
fact = factorial
# print(fact)
# print(fact(42))
# print(map(factorial, range(11)))
# print(list(map(fact, range(11))))
# print(list(map(factorial, filter(lambda n: n % 2, range(11)))))
l = [fact(n) for n in range(11)]
l2 = [factorial(n) for n in range(11) if n % 2]

print(dir(factorial))
# print(l)
# print(l2)

# print(reduce(add, range(100)))
# print(sum(range(100)))


# q = 7 // 3
# print(q)
# r = 7 % 3
# print(r)


def reverse(word):
    return word[::-1]


# print(reverse('test'))

owocki = ['truskawka', 'figa', 'jabłko', 'wiśnia', 'banan', 'kiwi']

# print(sorted(owocki, key=len))
# print(sorted(owocki, key=reverse))
# print(sorted(owocki, key=lambda word: word[::-1]))
