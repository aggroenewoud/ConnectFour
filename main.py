import game

class main:

    def __init__(self):

        start_input = input('Start game? y/n: ')

        while start_input != 'n':
            if start_input == 'y':
                game.game()
            start_input = input('Start game? y/n: ')

if __name__ == '__main__':
    main()
