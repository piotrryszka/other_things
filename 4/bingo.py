import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pobranie z pustej kuli')

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(10))
print(bingo.pick())
print(bingo())
print(callable(bingo))


class T: pass


ob = T()


def f(): pass


print(sorted(set(dir(f)) - set(dir(ob))))
