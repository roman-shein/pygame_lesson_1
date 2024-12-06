import pygame
import random
import sys


def draw(screen):
    screen.fill((0, 0, 0))
    colors = {0: "red", 1: "blue", 2: "green"}
    for i in range(n):
        pygame.draw.circle(screen, colors[i % 3], (width // 2, width // 2), w * (n - i))

if __name__ == '__main__':
    try:
        w, n = map(int, input().split())
    except ValueError:
        print("Неправильный формат ввода")
        sys.exit(0)
    pygame.init()
    size = width, height = 2 * w * n, 2 * w * n
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Шахматная клетка")
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()