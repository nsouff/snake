from enum import Enum
from linked_list import *
class Direction(Enum):
    N = 1
    E = 2
    S = 3
    W = 4
    def opposite(self, dir):
        return abs(self.value - dir.value) == 2
class Snake():
    def __init__(self, grid, size=3, speed=10):
        self.grid = grid
        self.speed = speed
        self.dir = Direction.E
        self.pos = LinkedList()
        self.score = 0
        for i in range(size):
            self.pos.add_last((len(grid)//2 - i, len(grid[0])//2))
            self.grid[len(grid)//2 - i][len(grid[0])//2] = 1

    def update(self):
        next_pos = None
        if self.dir == Direction.N:
            next_pos = (self.pos.first.item[0], self.pos.first.item[1] - 1)
        elif self.dir == Direction.E:
            next_pos = (self.pos.first.item[0] + 1, self.pos.first.item[1])
        elif self.dir == Direction.S:
            next_pos = (self.pos.first.item[0], self.pos.first.item[1] + 1)
        else:
            next_pos = (self.pos.first.item[0] - 1, self.pos.first.item[1])

        if len(self.grid[0]) > next_pos[1] and len(self.grid) > next_pos[0] and next_pos[0] >= 0 and next_pos[1] >= 0:
            i = self.grid[next_pos[0]][next_pos[1]]
            if i == 1:
                return 0
            elif i == 0:
                last_pos = self.pos.remove_last()
                self.grid[last_pos[0]][last_pos[1]] = 0
                self.pos.add_first(next_pos)
                self.grid[next_pos[0]][next_pos[1]] = 1
                return 1
            else: # i == 2
                self.speed += 1
                self.pos.add_first(next_pos)
                self.grid[next_pos[0]][next_pos[1]] = 1
                self.score += 1
            return 2
        else:
            return 0
    def turn(self, dir):
        if not dir.opposite(self.dir):
            self.dir = dir
            return True
        return False
