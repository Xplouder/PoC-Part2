"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid is not None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return row, col
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        :param move_string:
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][
                    zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][
                    zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][
                    zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][
                    zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        :param target_row:
        :param target_col:
        """
        if self.get_number(target_row, target_col) != 0:
            return False

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                # current value
                curr_v = self.get_number(row, col)
                # expected value
                expec_v = get_matrix_number(self.get_width(), row, col)
                if row > target_row and curr_v != expec_v:
                    return False
                if col > target_col and row == target_row and curr_v != expec_v:
                    return False

        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        :param target_row:
        :param target_col:
        """
        assert self.lower_row_invariant(target_row, target_col)
        row, column = self.current_position(target_row, target_col)
        movements_sequence = self.move_tile(target_row, target_col, row, column)
        self.update_puzzle(movements_sequence)
        assert self.lower_row_invariant(target_row, target_col - 1)
        return movements_sequence

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        :param target_row:
        """
        assert self.lower_row_invariant(target_row, 0)
        move_sequence = 'ur'
        self.update_puzzle(move_sequence)

        row, column = self.current_position(target_row, 0)
        # in case target tile is already in place
        if row == target_row and column == 0:
            # move tile zero to the right end of that row
            step = (self.get_width() - 2) * 'r'
            self.update_puzzle(step)
            move_sequence += step
        else:
            # target tile to position (i-1, 1)
            #   zero tile to position (i-1, 0)
            step = self.move_tile(target_row - 1, 1, row, column)
            # use move string for a 3x2 puzzle to bring target tile into
            # position (i, 0), then move tile zero to the right end of row i-1
            step += 'ruldrdlurdluurddlu' + (self.get_width() - 1) * 'r'
            self.update_puzzle(step)
            move_sequence += step

        assert self.lower_row_invariant(target_row - 1, self.get_width() - 1)
        return move_sequence

    def move_tile(self, target_row, target_col, current_row, current_column):
        """
        Move a tile from current position to target position.
        Target tile's current position must be either above the target position
        (k < i) or on the same current_row to the left (i = k and l < j);
        :return move_sequence: Represents the moves sequence to move the tile
        from current position to the target position
        """
        move_sequence = ''
        half_rotation_sequence = 'druld'

        # calculate diffs
        column_diff = target_col - current_column
        row_diff = target_row - current_row

        # move up
        move_sequence += row_diff * 'u'

        # tiles are in the same column
        if column_diff == 0:
            move_sequence += 'ld' + (row_diff - 1) * half_rotation_sequence
        else:
            # current tile is on the left of target tile
            if column_diff > 0:
                move_sequence += column_diff * 'l'
                if current_row == 0:
                    move_sequence += (column_diff - 1) * 'drrul'
                else:
                    move_sequence += (column_diff - 1) * 'urrdl'
            # current tile is on the right of target tile
            elif column_diff < 0:
                # absolute value
                column_diff *= -1
                move_sequence += (column_diff - 1) * 'r'
                if current_row == 0:
                    move_sequence += column_diff * 'rdllu'
                else:
                    move_sequence += column_diff * 'rulld'
            # apply common move as last
            move_sequence += row_diff * half_rotation_sequence

        return move_sequence

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        :param target_col:
        """
        if self.get_number(0, target_col) != 0:
            return False

        for column in range(self.get_width()):
            for row in range(self.get_height()):
                if (row == 0 and column > target_col) or \
                        (row == 1 and column >= target_col) or row > 1:
                    expect_v = get_matrix_number(self.get_width(), row, column)
                    current_v = self.get_number(row, column)
                    if expect_v != current_v:
                        return False

        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if not self.lower_row_invariant(1, target_col):
            return False

        for column in range(0, self.get_width()):
            for row in range(2, self.get_height()):
                expected_v = get_matrix_number(self.get_width(), row, column)
                current_v = self.get_number(row, column)
                if expected_v != current_v:
                    return False

        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        :param target_col:
        """
        assert self.row0_invariant(target_col)
        move_sequence = 'ld'
        self.update_puzzle(move_sequence)

        # unpack tile row and column values
        row, column = self.current_position(0, target_col)
        # got lucky, target tile already in place
        if row == 0 and column == target_col:
            return move_sequence
        else:
            # target tile to position (1, j-1) and zero tile to (1, j-2)
            step = self.move_tile(1, target_col - 1, row, column)
            # use move string for a 2x3 puzzle
            step += 'urdlurrdluldrruld'
            self.update_puzzle(step)
            move_sequence += step

        # assert self.row0_invariant(target_col - 1)
        return move_sequence

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # assert self.row1_invariant(target_col)
        row, column = self.current_position(1, target_col)
        move_it = self.move_tile(1, target_col, row, column)
        move_it += 'ur'

        self.update_puzzle(move_it)
        return move_it

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        move_sequence = ''
        first_step = ''

        if self.get_number(1, 1) == 0:
            first_step += 'ul'
            self.update_puzzle(first_step)
            # got lucky, all tiles are already in place
            if (0, 1) == self.current_position(0, 1) and \
                            (1, 1) == self.current_position(1, 1):
                return first_step

            # pick a move depending on current configuration
            if self.get_number(0, 1) < self.get_number(1, 0):
                move_sequence += 'rdlu'
            else:
                move_sequence += 'drul'
            self.update_puzzle(move_sequence)

        return first_step + move_sequence

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        move_sequance = ''

        # first off, need 0 tile in the right lower corner
        row = self.get_height() - 1
        column = self.get_width() - 1
        # unpack tile row and column values
        row_current, column_current = self.current_position(0, 0)
        # calculate deltas
        column_delta = column_current - column
        row_delta = row_current - row
        step = abs(column_delta) * 'r' + abs(row_delta) * 'd'
        self.update_puzzle(step)
        move_sequance += step

        # bottom m-2 rows in order from bottom to top and right to left
        for dummy_row in range(row, 1, -1):
            for dummy_column in range(column, 0, -1):
                move_sequance += self.solve_interior_tile(dummy_row, dummy_column)
            move_sequance += self.solve_col0_tile(dummy_row)

        # rightmost n-2 columns of the top two rows in a bottom to top and right to left order
        for dummy_column in range(column, 1, -1):
            move_sequance += self.solve_row1_tile(dummy_column)
            move_sequance += self.solve_row0_tile(dummy_column)

        # what's left unsolved is upper left 2 by 2 portion
        move_sequance += self.solve_2x2()
        return move_sequance


def get_matrix_number(matrix_width, coord_x, coord_y):
    """
    Given any matrix, return the "standard unique" value on matrices with first
    of zero.
    :param matrix_width:
    :param coord_x:
    :param coord_y:
    :return:
    """
    return coord_x * matrix_width + coord_y

# Start interactive simulation
# poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
