#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run connect-stars

# In this mission you'll have to make theMinimum spanning tree (Wikipedia).
# 
# You are given a list of coordinates of vertices. Each coordinate is a tuple of x (integer) and y (integer).
# You have to return a list (or an iterable) of lines that connect all vertices.    The total length of lines should be the minimum. Each line is a tuple of two integers.     These integers represent the index of list of input.
# 
# NOTE:
# 
# The output of tests has a unique combination of lines.Input:A list of coordinates of vertices.Each coordinate is a tuple of x (integer) and y (integer).
# 
# Output:A list (or an iterable) of lines.Each line is a tuple of two integers. These integers represent the index of list of input.The order of lines and each index is arbitrary (see examples).
# 
# Precondition:2 ≤ len(input) ≤ 500 ≤ x (,y) ≤ 999
# 
# 
# END_DESC

from typing import List, Tuple, Iterable


def connect_stars(coords: List[Tuple[int, int]]) -> Iterable[Tuple[int, int]]:
    # your code here
    return []


if __name__ == '__main__':

    print("Example:")
    print(connect_stars([(1, 1), (4, 4)]))

    def sort_edges(edges): return sorted(map(lambda e: tuple(sorted(e)), edges))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_edges(connect_stars([(1, 1), (4, 4)])) == [(0, 1)], '2 vertices'
    assert sort_edges(connect_stars([(1, 1), (4, 1), (4, 4)])) == [(0, 1), (1, 2)], '3 vertices'
    assert sort_edges(connect_stars([(6, 6), (6, 8), (8, 4), (3, 2)])) == [(0, 1), (0, 2), (0, 3)], '4 vertices'
    assert sort_edges(connect_stars([(5, 4), (5, 1), (2, 6), (7, 2), (6, 9)])) == [(0, 2), (0, 3), (1, 3), (2, 4)], '5 vertices'
    assert sort_edges(connect_stars([(5, 8), (5, 1), (4, 2), (7, 6), (8, 6), (2, 2)])) == [(0, 3), (1, 2), (2, 3), (2, 5), (3, 4)], '6 vertices'
    assert sort_edges(connect_stars([(2, 7), (9, 9), (4, 9), (9, 6), (3, 3), (1, 6), (9, 7)])) == [(0, 2), (0, 5), (1, 2), (1, 6), (3, 6), (4, 5)], '7 vertices'
    print("Coding complete? Click 'Check' to earn cool rewards!")