
# scalenie dwóch obrazów w jeden za pomocą Pygame

from pygame import image, Rect

maze = image.load('maze.png')
player = image.load('player.png')

maze.blit(player, Rect((32, 32, 64, 64)), Rect((0, 0, 32, 32)))
image.save(maze, 'merged.png')
