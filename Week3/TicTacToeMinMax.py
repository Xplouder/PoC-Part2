"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
try:
    import codeskulptor
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor

codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

DEBUG_BOARDS = [[]]
DEBUG_MM = False
RECURSIVE_COUNTER = 0


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements:
        - The first element is the score of the given board
        - The second element is the desired move as a tuple, (row, col).
    :param board:
    :param player:
    """
    # --------------------------------------------------------------------------
    global DEBUG_BOARDS, RECURSIVE_COUNTER
    if DEBUG_MM:
        RECURSIVE_COUNTER += 1
        tree_depth = board.get_dim() ** 2 - len(board.get_empty_squares())
        while len(DEBUG_BOARDS) < tree_depth+2:
            DEBUG_BOARDS.append([])
        DEBUG_BOARDS[tree_depth].append(board)
    # --------------------------------------------------------------------------

    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)

    opponent = provided.switch_player(player)
    # initialization with "worst" possible values
    player_move = SCORES[opponent], (-1, -1)

    for square in board.get_empty_squares():
        board_clone = board.clone()
        board_clone.move(square[0], square[1], player)

        opponent_move = mm_move(board_clone, opponent)
        if opponent_move[0] * SCORES[player] > player_move[0] * SCORES[player]:
            player_move = opponent_move[0], square

        if player_move[0] == SCORES[player] or board_clone.check_win() == player:
            return player_move

    return player_move


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    :param board:
    :param player:
    :param trials:
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

if DEBUG_MM:
    for depth in range(len(DEBUG_BOARDS)):
        print "Depth:", depth
        for board in (DEBUG_BOARDS[depth]):
            print board
    print "Recursive counts: " + str(RECURSIVE_COUNTER)
