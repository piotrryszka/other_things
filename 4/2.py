def main():
    global owocki
    owocki = ['truskawka', 'figa', 'jabłko', 'wiśnia', 'banan', 'kiwi']


def listing(owocki=None):
    a = 1
    print(owocki)


def addon():
    lista1 = [9, 4, 5, 8, 7, 5]
    lista2 = [91, 24, 35, 58, 67, 35]

    lista3 = lista1 + lista2
    print(lista3)


if __name__ == '__main__':
    # owocki = 47387
    # main()
    # listing(owocki)
    addon()
