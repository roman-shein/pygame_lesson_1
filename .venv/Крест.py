import pygame
import random
import sys


def draw(screen):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, 'white', (0, 0), (width - 1, height - 1), 5)
    pygame.draw.line(screen, 'white', (0, height - 1), (width - 1, 0), 5)


if __name__ == '__main__':
    try:
        w, h = map(int, input().split())
    except ValueError:
        print("Неправильный формат ввода")
        sys.exit(0)
    pygame.init()
    size = width, height = w, h
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Крест")
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()