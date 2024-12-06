import pygame
import random
import sys


def draw(screen):
    screen.fill((0, 0, 0))
    screen.fill(pygame.Color("red"), pygame.Rect(1, 1, width - 2, height - 2))


if __name__ == '__main__':
    try:
        w, h = map(int, input().split())
    except ValueError:
        print("Неправильный формат ввода")
        sys.exit(0)
    pygame.init()
    size = width, height = w, h
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Прямоугольник")
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()