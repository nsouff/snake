import pygame
from pygame.locals import *
from snake import *
from linked_list import *

class Game():
    def __init__(self, width=80, height=80):
        self.foods = []
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.snake = Snake(self.grid)
    def add_food(self):
        self.foods.append((1, 5))
        self.grid[0][0] = 2
def update_render(game, window):
    window.fill((0,0,0))
    it = game.snake.pos.first
    while it != None:
        pygame.draw.rect(window, (255, 255, 255), (it.item[0] * 10, it.item[1] * 10, 10, 10))
        it = it.next
    for food in game.foods:
        pygame.draw.circle(window, (255, 0, 0), (food[0]*10+5, food[1]*10+5), 5)
    pygame.display.flip()
def main():
    game = Game()
    pygame.init()
    pygame.display.set_caption("Snake")
    window = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    update_render(game, window)
    running = 1
    next_food = pygame.time.get_ticks() + 5000
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    game.snake.turn(Direction.N)
                elif event.key == K_RIGHT:
                    game.snake.turn(Direction.E)
                elif event.key == K_DOWN:
                    game.snake.turn(Direction.S)
                elif event.key == K_LEFT:
                    game.snake.turn(Direction.W)
        i = game.snake.update()
        if i == 0:
            running = 0
        else :
            actual = pygame.time.get_ticks()
            if actual >= next_food:
                game.add_food()
            update_render(game, window)
            clock.tick(game.snake.speed)
if __name__ == '__main__':
    main()
