from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    current_player = 'X'
    running = True
    game = Board()
    game.display()
    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 1 or row > game.field_size:
                    raise FieldIndexError
                col = int(input('Введите номер столбца: '))
                if col < 1 or col > game.field_size:
                    raise FieldIndexError
                if game.board[row - 1][col - 1] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print('Введено некорректное значение. Попробуй еще раз!')
                continue
            except ValueError:
                print('Хитрец, вводить можно только целые числа! '
                      'Попробуй еще раз!')
                continue
            except CellOccupiedError:
                print('Ячейка занята. Попробуй снова!')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue
            else:
                break
        game.make_move(row - 1, col - 1, current_player)
        print('Ход сделан!')
        game.display()
        if game.check_win(current_player):
            print('Конец игры!')
            result = f'Победил игрок: {current_player}'
            print(result)
            save_result(result)
            running = False
        if game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
            running = False
        current_player = 'X' if current_player == 'O' else 'O'


def save_result(message):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(message + '\n')


if __name__ == '__main__':
    main()
