# Z BŁĘDAMI!
# Ten kod zawiera co najmniej 9 defektów.
# Spróbuj je naprawić na podstawie komunikatów o błędach.

import pygame
from pygame import image, Rect


TILE_POSITIONS =[
    ('#', 0, 0),  # ściana
    (' ', 0, 1),   # podłoga
    ('.', 2, 0),  # punkt
]
SIZE = 32

image = 'tiles.xpm'


def load_tiles():
    """
    Ładuje kafelki z pliku graficznego do słownika.
    Zwraca krotkę w postaci (obraz, kafelek_dict)
    """
    tiles = {}
    tile_img = image.load('tiless.xpm')
    for x, y in TILEPOSITIONS:
        rect = Rect(x*SIZE, y*SIZE, SIZE, SIZE)
        tiles[symbol] = rect
    return tile_img, tiles


if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    m = Surface((96, 32))
    m.blit(tile_img, get_tile_rect(0, 0), tiles['#'])
    m.blit(tile_img, get_tile_rect(1, 0), tiles[' '])
    m.blit(tile_img, get_tile_rect(2, 0), tiles['*'])
    image.save(m, 'tile_combo.png')


# ----------------------------

# Ćwiczenie opcjonalne:
# przekształć kod tak, aby działała poniższa instrukcja print.
# Zmodyfikuj klasę tak,
# aby wyświetlała atrybut char


class Tile:

    def __init__(self, achar, x, y):
        char = achar

t = Tile('#', 0, 0)
print(t.char)
