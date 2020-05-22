import pygame
from pygame.locals import *
from snake import *
from linked_list import *

def update_render(snake, window):
    it = snake.pos.first
    while it != None:
        print(it.item)
        pygame.draw.rect(window, (255, 255, 255), (it.item[0] * 10, it.item[1] * 10, 10, 10))
        it = it.next
    pygame.display.flip()
def main():
    grid = [[0 for _ in range(80)] for _ in range(80)]
    snake = Snake(grid)
    pygame.init()
    pygame.display.set_caption("Snake")
    window = pygame.display.set_mode((800, 800))
    window.fill((0, 0, 0))
    update_render(snake, window)
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0

if __name__ == '__main__':
    main()
