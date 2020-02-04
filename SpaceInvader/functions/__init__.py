import pygame
import math


def screen_size(x, y):
    return pygame.display.set_mode((x, y))


def background(path):
    return pygame.image.load(path).convert()


def distance_between_two_points(a, b, c, d, dist=27):
    distance = math.sqrt((a - c) ** 2 + (b - d) ** 2)
    if distance < dist:
        return True
    else:
        return False

