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
class ScoreTest(unittest.TestCase):
    def test_add_score(self):
        score = Score()
        score.add_score('Nathan', 10)
        score.add_score('Nathan', 12)
        score.add_score('Nat', 5)
        score.add_score('N', 20)
        score.add_score('Nathan', 0)
        score.add_score('N', 1)
        score.add_score('a', 19)
        score.add_score('b', 15)
        score.add_score('c', 0)
        score.add_score('c', 20)
        score.add_score('d', 15)
        score.add_score('d', 15)
        self.assertEqual(len(score.scores), 10)
        scores = [('c', 20), ('N', 20), ('a', 19), ('d', 15), ('d', 15), ('b', 15), ('Nathan', 12), ('Nathan', 10), ('Nat', 5), ('N', 1)]
        self.assertListEqual(score.scores, scores)
if __name__ == '__main__':
    unittest.main()
