import pygame
from pygame.locals import *
from snake import *
from linked_list import *
import random

class Game():
    def __init__(self, width=40, height=40):
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
                if y < self.height - 1:
                    y += 1
                elif x < self.width - 1:
                    y = 0
                    x += 1
                else:
                    x = 0
                    y = 0
            self.grid[x][y] = 2
            self.foods.append((x, y))
