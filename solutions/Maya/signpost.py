#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run signpost

# This mission is an adaptation of the "Signpost" game (fromSimon Tatham's Portable Puzzle Collection).    If you are lost or just want to play, the game is availablehere.
# 
# 
# 
# You're on a rectangular grid. You must find your way to go through    the entire grid, following the directions indicated. Some boxes are already    given like the start and the end of the path, you have to respect them.
# 
# The numbers say the location in the path, starting at 1. For example,    a box with the number 9 indicates that this box is the ninth on the path.
# 
# Empty boxes are represented by zeros.    Possible directions:    north 'N', northwest 'NW', west 'W', southwest 'SW',    south 'S', southeast 'SE', east 'E', northeast 'NE'    and nothing '' (for the end of the path).
# 
# Then, you have to return the completed grid representing the path.
# 
# Input:A list of lists of integers, and a tuple of tuples of strings.
# 
# Output:A list/tuple of lists/tuples of integers.
# 
# Preconditions:Given puzzles are solvable and have only one solution.3 ≤ len(grid) ≤ 30 and 3 ≤ len(grid[0]) ≤ 50.len(grid) == len(directions) and all(len(row1) == len(row2) == len(grid[0]) for row1, row2 in zip(grid, directions)).
# 
# 
# END_DESC

def signpost(grid, directions):
    return grid


if __name__ == '__main__':
    def checker(func, grid, directions):
        result = func([row[:] for row in grid], directions)
        nb_rows, nb_cols = len(grid), len(grid[0])
        N = nb_rows * nb_cols
        # check types
        if not (isinstance(result, (list, tuple)) and
                all(isinstance(row, (list, tuple)) and
                    all(isinstance(n, int) for n in row) for row in result)):
            print("Result should be a list/tuple of lists/tuples of integers.")
            return False
        # check sizes and content compatibility
        if not (len(result) == nb_rows and
                all(len(row) == nb_cols for row in result)):
            print("You should not have changed sizes.")
            return False
        if not all(user_n == n for row, user_row in zip(grid, result)
                               for n, user_n in zip(row, user_row) if n):
            print("You should not have changed non-zero numbers.")
            return False
        # check if numbers describe range(1, N + 1)
        numbers = sorted(n for row in result for n in row)
        if 0 in numbers:
            print("Still a zero in the grid.")
            return False
        if numbers != list(range(1, N + 1)):
            print(f"Numbers in the grid should be integers between 1 and {N}.")
            return False
        path = {n: (i, j) for i, row in enumerate(result)
                          for j, n in enumerate(row)}
        vectors = {'NW': (-1, -1), 'N': (-1, 0), 'NE': (-1, 1),
                   'W' : ( 0, -1),               'E' : ( 0, 1),
                   'SW': ( 1, -1), 'S': ( 1, 0), 'SE': ( 1, 1)}
        same_direction = lambda x1, y1, x2, y2: (x1 * y2 == x2 * y1 and
                                                 x1 * x2 >= 0 and y1 * y2 >= 0)
        for n in range(1, N):
            (i, j), (x, y) = path[n], path[n + 1]
            vector, nwse = (x - i, y - j), directions[i][j]
            if not same_direction(*vector, *vectors[nwse]):
                print(f"Arrow from {n} to {n + 1}: "
                      f"direction at {(i, j)} is not respected.")
                return False
        return True

    TESTS = (([[1, 0, 0],
               [0, 0, 0],
               [0, 0, 9]],
              (('S', 'E', 'S'),
               ('S', 'S', 'NW'),
               ('NE', 'NE', ''))),

             ([[16, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]],
              (('', 'E', 'SW', 'W'),
               ('E', 'SE', 'S', 'W'),
               ('SE', 'SE', 'NW', 'N'),
               ('NE', 'W', 'NE', 'N'))),

             ([[1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 24]],
              (('SE', 'E', 'SW', 'W', 'S', 'S'),
               ('E', 'E', 'SE', 'W', 'NW', 'S'),
               ('E', 'E', 'SW', 'W', 'SW', 'S'),
               ('E', 'W', 'NE', 'NW', 'NW', ''))),

             ([[1, 0, 0, 0, 0],
               [0, 0, 9, 0, 18],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 25]],
              (('SE', 'E', 'SW', 'S', 'S'),
               ('E', 'W', 'S', 'NE', 'SW'),
               ('S', 'N', 'N', 'N', 'S'),
               ('NE', 'N', 'NE', 'SE', 'W'),
               ('NE', 'NE', 'W', 'W', ''))))

    for n, (grid, directions) in enumerate(TESTS, 1):
        assert checker(signpost, grid, directions), f"example #{n}"