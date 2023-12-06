import numpy as np
from board import *

init_state = [[1,1,1,1,1], 
            [1,0,0,0,1], 
            [1,0,0,0,-1], 
            [-1,0,0,0,-1], 
            [-1,-1,-1,-1,-1]]
board = Board(init_state)
# board.board: 1D array
#move: tuple (start, end)
#player: +1 -> MAX, -1 -> MIN
# board.makeMove(move, player)

def get_dataset():
    """
    Parse checkers OCA dataset and save as numpy array

    0-0: 0  -> draw
    0-1: 1  -> green wins
    1-0: -1 -> red wins
    """

    states, values = [], []
    value = {'0-0': 0, '0-1': 1, '1-0': -1}
    n_games = {'0-0': 0, '0-1': 0, '1-0': 0}
    parsed_game = 0
    # hasPrint = False
    with open('data.txt') as file:
        for part in file.read().split('\n\n'):
            tokens = part.split()
            val = tokens[-1]
            n_games[val] = n_games[val] + 1
            print(f'Parsing game {parsed_game}')

            board = Board(init_state)
            skiping = True
            player = PLAYER_MIN
            for token in tokens:
                if skiping is True:
                    if token == '1.':
                        skiping = False
                    continue
                else:
                    if '.' in token or token == val:
                        continue
                    else:
                        t = token.split('-')
                        try:
                            move = [int(t[0]), int(t[1])]
                        except:
                            break
                        # play_move(board, move, turn)
                        board.makeMove(move, player)
                        # print_board(board)
                        # print()

                    states.append(board.board)

                    # if hasPrint == False:
                    #     print("----- Board -----")

                    #     res = ""
                    #     for z in range(len(board.board)):
                    #         if (z % 5 == 0): res += "\n"
                    #         res += str(board.board[z]) + " "
                    #     print(res)
                            

                    # states.append(map_state(board))
                    values.append(value[val])
                    player = PLAYER_MAX if player == PLAYER_MIN else PLAYER_MIN
                    # turn = Turn.BLACK if turn == Turn.WHITE else Turn.WHITE

                    # x = list board_state
                    # y = list value = result
            parsed_game += 1

            # hasPrint = True

    print(f'0-0 -> {n_games["0-0"]}')
    print(f'0-1 -> {n_games["0-1"]}')
    print(f'1-0 -> {n_games["1-0"]}')

    x, y = np.array(states), np.array(values)
    np.savez("data/processed.npz", x, y)

# get_dataset()