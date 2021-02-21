#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run simple-areas

# Stephan works with simple forms when constructing something,    and he need some programming tools to calculate his expenses.    Let's take a trip back to our school days and pull out some simple geometry for this.
# 
# You should write a function to calculate the area of simple figures: circles, rectangles and triangles.    You are give an arbitrary number of arguments and depending on this,    the function calculates area for the different figures.
# 
# One argument -- The diameter of a circle and you need calculate the area of the circle.Two arguments -- The side lengths of a rectangle and you need calculate the area of the rectangle.Three arguments -- The lengths of each side on a triangle and you need calculate the area of the triangle.
# 
# The result should be given with two digits precision as ±0.01.
# 
# Tips:Think about how to work withan arbitrary number of        arguments.
# 
# Input:One, two or three arguments as floats or as integers.
# 
# Output:The area of the circle, the rectangle or the triangle as a float.
# 
# Precondition:
# 0 < len(args) ≤ 3
# all(0 < x ≤ 1000 for x in args)
# For "triangle" cases the sum of the lengths of any two sides always exceeds the length of the third side.
# 
# 
# END_DESC

import math
def simple_areas(*args):
    S = 0
    if len(args) == 1:        
        S = 0.25 * math.pi * args[0] ** 2
    elif len(args) == 2:
        S = args[0] * args[1]
    else:
        p = (args[0] + args[1] + args[2]) / 2
        S = math.sqrt(p * (p - args[0]) * (p - args[1]) * (p - args[2]))
    return S

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"