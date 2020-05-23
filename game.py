import pygame
from pygame.locals import *
from snake import *
from linked_list import *
import random

class Game():
    def __init__(self, width=80, height=50):
        self.width = width
        self.height = height
        self.foods = []
        self.grid = [[0 for _ in range(height)] for _ in range(width)]
        self.snake = Snake(self.grid)
    def add_food(self):
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        if self.grid[x][y] == 0:
            self.grid[x][y] = 2
            self.foods.append((x, y))
        else:
            while self.grid[x][y] != 0:
                if y < height - 1:
                    y += 1
                elif x < width - 1:
                    y = 0
                    x += 1
                else:
                    x = 0
                    y = 0
            self.grid[x][y] = 2
            self.foods.append((x, y))
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
    window = pygame.display.set_mode((game.width*10, game.height*10))
    clock = pygame.time.Clock()
    update_render(game, window)
    running = 1
    next_food = pygame.time.get_ticks() + 5000
    while running:
        dir_change = False
        for event in pygame.event.get():

            if event.type == QUIT:
                running = 0
            elif event.type == KEYDOWN and not dir_change:
                if event.key == K_UP:
                    dir_change = game.snake.turn(Direction.N)
                elif event.key == K_RIGHT:
                    dir_change = game.snake.turn(Direction.E)
                elif event.key == K_DOWN:
                    dir_change = game.snake.turn(Direction.S)
                elif event.key == K_LEFT:
                    dir_change = game.snake.turn(Direction.W)
        i = game.snake.update()
        if i == 0:
            running = 0
        else :
            if i == 2:
                game.foods.remove(game.snake.pos.first.item)
            actual = pygame.time.get_ticks()
            if actual >= next_food:
                game.add_food()
                next_food = pygame.time.get_ticks() + 5000
            update_render(game, window)
            clock.tick(game.snake.speed)
if __name__ == '__main__':
    main()
