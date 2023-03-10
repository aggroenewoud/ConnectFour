import board
import player
import bot

class game:

    def __init__(self):

        self.board = board.board(6, 7)

        self.game_ongoing = self.board.board_filled()

        self.players = [
            None,
            None
        ]

        self.select_players()

        self.start_game()

    def start_game(self):

        self.board.print_board()

    def select_players(self):

        options = [
            player.player,
            bot.bot
        ]

        print('Select player1: ')
        user_choice1 = int(input('1. User / 2.Bot : ')) -1

        self.players[0] = options[user_choice1]()

        print('Select player2: ')
        user_choice2 = int(input('1. User / 2.Bot : ')) -1

        self.players[1] = options[user_choice2]()

        if self.players[0] and self.players[1]:
            return
