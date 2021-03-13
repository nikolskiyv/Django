import unittest
from hw1 import TicTacGame

class TestTicTacGame(unittest.TestCase):
    
    def setUp(self):
        self.game = TicTacGame()
    
    def test_validate_input(self):
        self.assertEqual(self.game.validate_input(10), False)
        self.assertEqual(self.game.validate_input("f"), False)
        self.assertEqual(self.game.validate_input(5), True)
        self.assertEqual(self.game.validate_input(0), False) 

        self.game.board[6] = "X"
        self.assertEqual(self.game.validate_input(7), False)

    def test_check_winner(self):
        self.game.board[0] = "X"
        self.game.board[1] = "X"
        self.game.board[2] = "X"
        self.assertEqual(self.game.check_winner(), True)
        #self.game.board[0] = "X"
        #self.game.board[1] = "X"
        #self.game.board[2] = "O"
        #self.game.board[3] = "X"
        #self.assertEqual(self,game.check_winner(), False)

    def test_player(self):
        self.counter = 5
        self.assertEqual(self.game.player(), 1)
        #self.counter += 1
        #self.assertEqual(self.game.player(), 2)

if __name__ == '__main__':
    unittest.main()
