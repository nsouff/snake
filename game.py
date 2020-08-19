import pygame
from pygame.locals import *
from snake import *
from linked_list import *
import pickle
import random
import os

score = None
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

class Score():
    def __init__(self, max_len=10, filename='.score'):
        self.filename = filename
        self.max_len = max_len
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                self.scores = pickle.load(f)
        else:
            self.scores = []
    def add_score(self, name, score):
        act_len = len(self.scores)
        if self.max_len > act_len or score >= self.scores[self.max_len-1][1]:
            self.__add_score_aux(name, score)
            if act_len == self.max_len:
                self.scores.pop()
    def __add_score_aux(self, name, score, start=None, end=None):
        if start == None:
            start = 0
        if end == None:
            end = len(self.scores)
        if end == start:
            self.scores = self.scores[:start] + [(name, score)] + self.scores[start:]
            return
        middle = (end + start) // 2
        if score < self.scores[middle][1]:
            return self.__add_score_aux(name, score, start=middle+1, end=end)
        else:
            return self.__add_score_aux(name, score, start=start, end=middle)

    def save_score(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.scores, f)
    def get_highest(self):
        if len(self.scores) == 0:
            return 0
        else:
            return self.scores[0][1]
    @classmethod
    def init_score(cls):
        cls.score = Score()
    @classmethod
    def reset_scores(cls):
        os.remove(cls.score.filename)
        cls.score.scores = []
