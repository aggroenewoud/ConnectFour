class board:

    def __init__(self, row, column):

        self.board = self.create_board(row, column)

    def create_board(self, row, column):

        board = []

        for x in range(row):

            board_column = []

            for y in range(column):

                board_column.append(' ')

            board.append(board_column)

        return board

    def print_board(self):

        board = self.board

        for x in range(len(board)):

            line = str(x + 1) + ' |'

            for y in range(len(board[0])):

                line += board[x][y] + '|'

            print(line)

        y_index = '   '

        for i in range(len(board[0])):
            y_index += str(i + 1) + ' '

        print(y_index)
