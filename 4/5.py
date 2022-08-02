import time


def dekor(funkcja):
    def wew(*args, **kwargs):
        start = time.time()
        x = funkcja(*args, **kwargs)
        koniec = time.time()
        print(funkcja.__name__, "wykonywała się", koniec - start, "sek.")
        return x

    return wew


@dekor
def pierwsza(a, b):
    time.sleep(1)
    return a + b


@dekor
def druga(a, b, c):
    time.sleep(0.5)
    return a - b - c


print(pierwsza(2, 3))
print(druga(3, 2, 1))
