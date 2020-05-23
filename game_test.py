from game import *
import unittest
class GameTest(unittest.TestCase):
    def test_add_food(self):
        x = 50
        y = 60
        game = Game(x, y)
        for i in range(x * y -3): # fill all the grid (already 3 snake case in the grid)
            game.add_food()
        for i in range(x):
            for j in range(y):
                self.assertNotEqual(game.grid[i][j], 0)

if __name__ == '__main__':
    unittest.main()
