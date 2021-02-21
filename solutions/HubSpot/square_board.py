#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run square-board

# You are designing a board gamein which tokens move around the square board with. (like inMonopoly (Wikipedia))
# 
# You need to write the function that returns the coordinates after the token has moved. The coordinates of a token are being represented by a tuple consisting of a row and column. The coordinates of a top-left one - (0, 0).
# 
# You are given three arguments:the first one is the length of the game board’s side (an integer);the second is the token’s current position (an integer);Cells around the board are numbered clockwise starting with 0 on the bottom right corner.
# 
# the third is the number of steps to advance (an integer);A positive number represents a clockwise direction. A negative number represents  a counterclockwise direction.
# 
# Input:3 arguments: the length of the game board’s side (an integer), token’s current position (an integer), and the number of steps to advance (an integer).
# 
# Output:The coordinates after the token has moved (a tuple consisting of a row and column).
# 
# How it is used:
# To get the coordinates of an object that moves around.
# 
# Precondition:
# 3 ≤ The length of the side ≤ 110 ≤ The position of the token < (side-1)*4
# 
# 
# END_DESC

from typing import Tuple
Coordinate = Tuple[int, int]


def square_board(side: int, token: int, steps: int) -> Coordinate:
    return (0, 0)

if __name__ == '__main__':
    print("Example:")
    print(square_board(4, 1, 4))
    assert square_board(4, 1, 4) == (1, 0)
    assert square_board(6, 2, -3) == (4, 5)

    print("Coding complete? Click 'Check' to earn cool rewards!")