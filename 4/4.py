import bobo


@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person


def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def dodaj(a, b):
    return a + b


def glowna():
    def wew2(a, b):
        return a * b

    return wew2


def dekor(funkcja):
    def wew(*args, **kwargs):
        print("Dekorujemy....:)")
        return funkcja(*args, **kwargs)

    return wew


@dekor
def zwykla(a, b, c):
    print("To jest zwykła funkcja")
    print(a + b + c)


nowa2 = zwykla
print(nowa2(3, 4, 5))

# nowa = dekor(zwykla)
# print(nowa())
# x = glowna()
# print(x(3, 3))
# print(wykonaj(dodaj, 2, 3))
