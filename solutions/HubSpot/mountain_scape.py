#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run mountain-scape

# You are given the coordinates of the tops of the triangles as input values.The slope angle is 45 degrees.The base is always on the x-axis.You must return the total area of all triangles.But count the overlapping areas only once.
# 
# NOTE:The sum of the X and Y coordinates is always even. (e.g. (1, 3) (0, 2) ...)
# 
# Input:A list of a tuple of two integers.
# 
# Output:An integer.
# 
# Precondition:
# 0 ≤ x ≤ 1001 ≤ y ≤ 50(x+y) % 2 == 01 ≤ len(tops) ≤ 50
# 
# 
# 
# 
# END_DESC

from typing import List, Tuple


def mountain_scape(tops: List[Tuple[int, int]]) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    print("Example:")
    print(mountain_scape([(1, 1), (4, 2), (7, 3)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mountain_scape([(1, 1), (4, 2), (7, 3)]) == 13
    assert mountain_scape([(0, 2), (5, 3), (7, 5)]) == 29
    assert mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]) == 37
    print("Coding complete? Click 'Check' to earn cool rewards!")