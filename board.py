class board:

    def __init__(self):

        pass

    def create_board(self, row, column):

        board = []

        for x in range(row):

            board_column = []

            for y in range(column):

                board_column.append(' ')

            board.append(board_column)

        return board
