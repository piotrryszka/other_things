
# Kod do rozdziału 02 - Wyjątki w Pythonie

from pygame import image, Rect, Surface

TILE_POSITIONS = [
    ('#', 0, 0),  # ściana
    (' ', 0, 1),   # podłoga
    ('x', 1, 1),  # wyjście
    ('.', 2, 0),   # punkt
    ('*', 3, 0),  # gracz
]
SIZE = 32


def get_tile_rect(x, y):
    """Konwertuje indeksy kafelków na obiekty pygame.Rect"""
    return Rect(x * SIZE, y * SIZE, SIZE, SIZE)


def load_tiles():
    """
    Ładuje kafelki z pliku graficzbego do słownika.
    Zwraca krotkę w postaci (obraz, kafelek_dict)
    """
    tile_image = image.load('../images/tiles.xpm')
    tiles = {}
    for symbol, x, y in TILE_POSITIONS:
        tiles[symbol] = get_tile_rect(x, y)
    return tile_image, tiles


if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    m = Surface((96, 32))
    m.blit(tile_img, get_tile_rect(0, 0), tiles['#'])
    m.blit(tile_img, get_tile_rect(1, 0), tiles[' '])
    m.blit(tile_img, get_tile_rect(2, 0), tiles['*'])
    image.save(m, 'tile_combo.png')
