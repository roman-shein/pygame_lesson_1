import pygame
import random
import sys


def draw(screen):
    screen.fill((0, 0, 0))
    c = 1
    d = a // n
    for row in range(n):
        for col in range(n):
            if (row + col) % 2 != 0:
                pygame.draw.rect(screen, pygame.Color("white"), (col * d, row * d, d, d))


if __name__ == '__main__':
    try:
        a, n = map(int, input().split())
    except ValueError:
        print("Неправильный формат ввода")
        sys.exit(0)
    pygame.init()
    size = width, height = a, a
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Шахматная клетка")
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()