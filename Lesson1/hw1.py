"""
HomeWork №1 by Nikolskiy Vladimir
"""

class TicTacGame:
    """ok"""

    board = list(range(1, 10))
    counter = 0

    def show_board(self):
        """ok"""

        print("------------")
        for i in range(3):
            print("|", self.board[0+i*3], "|", self.board[1+i*3], "|", self.board[2+i*3], "|")
            print("------------")

    def player(self):
        """ok"""
        if self.counter % 2 == 0:
            return 1
        return 2

    def validate_input(self, move):
        """ok"""
        try:
            move = int(move)
        except ValueError:
            print("> ! < Invalid input. Enter the number.")
            return False
        if 1 <= move <= 9:
            if str(self.board[move-1]) not in "XO":
                if self.player() == 1:
                    self.board[move-1] = "X"
                else:
                    self.board[move-1] = "O"
                return True
            print("> ! < This cell is already taken.")
            return False
        print("> ! < Please enter a number from 1 to 9.")
        return False

    def start_game(self):
        """ok"""

        win = False
        while win is False:
            valid = False
            while valid is False:
                if self.player() == 1:
                    self.show_board()
                    print("P1, make a move.")
                    print("-----")
                else:
                    self.show_board()
                    print("P2, make a move.")
                    print("-----")
                move = input()
                if self.validate_input(move) is True:
                    valid = True
                    self.counter += 1
            if self.counter > 4:
                win = self.check_winner()
                if win:
                    self.counter -= 1
                    if self.player() == 1:
                        print("> P1 - winner. <")
                    else:
                        print("> P2 - winner. <")
                    self.show_board()
                    break
                if self.counter == 9:
                    print("> Draw. <")
                    self.show_board()
                    break

    def check_winner(self):
        """ok"""
        win_comb = ((0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6))
        for each in win_comb:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return True
        return False

if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
