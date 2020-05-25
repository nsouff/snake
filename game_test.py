from game import *
import unittest
import os
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
    @classmethod
    def setUpClass(cls):
        if os.path.exists('.score_test'):
            os.remove('.score_test')
        cls.score = Score(filename='.score_test')
        cls.score.add_score('Nathan', 10)
        cls.score.add_score('Nathan', 12)
        cls.score.add_score('Nat', 5)
        cls.score.add_score('N', 20)
        cls.score.add_score('Nathan', 0)
        cls.score.add_score('N', 1)
        cls.score.add_score('a', 19)
        cls.score.add_score('b', 15)
        cls.score.add_score('c', 0)
        cls.score.add_score('c', 20)
        cls.score.add_score('d', 15)
        cls.score.add_score('d', 15)
        cls.result = [('c', 20), ('N', 20), ('a', 19), ('d', 15), ('d', 15), ('b', 15), ('Nathan', 12), ('Nathan', 10), ('Nat', 5), ('N', 1)]

    def test_add_score(self):
        self.assertEqual(len(ScoreTest.score.scores), 10)
        self.assertListEqual(ScoreTest.score.scores, ScoreTest.result)
    def test_open_and_close(self):
        self.score.save_score()
        score = Score(filename='.score_test')
        self.assertListEqual(ScoreTest.score.scores, self.result)
        os.remove('.score_test')

if __name__ == '__main__':
    unittest.main()
