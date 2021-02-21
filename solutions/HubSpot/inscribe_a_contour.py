#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run inscribe-a-contour

# Over the past almost 15 years,3D printinghas become very popular, not only amongst the big industrial companies which can afford to buy a super expensive        3D manufacturing complex (e.i.SLMorSLSmachines), but also among ordinary people, engineers and enthusiasts. It started in 2005 with theRepRapproject  within the University of Bath.        The project's main objective was to develop an affordable production system that would enable the production of cheap everyday household goods        regardless of the household's location. The project was successful and gave birth to the printer called "Darwin" at the beginning of 2008.        It was a fully open project under the GNU GPL and by the end of 2008th ~100 copies of "Darwin" have been produced in various countries.        Since then, there has been an exponential increase in the number of printers manufactured, both DIY and commercial.        Most of theFDMprinters you may find today in libraries, universities, workshops, engineering companies,        friend's houses are likely to be direct descendants of that very first desktop printer.        I do not possess any more up to date information, but in 2013 it's been sold ~72.000 of desktop printers, in 2014 - almost 140.000        (according to theWohlers Report).
# 
# 
# Leaving aside the 3D design process, which is the first step on the way to something to be printed, we go straight to preparing a 3D model for printing.            There's a variety of software applications designed for that purpose calledslicers. They slice a 3D model from the bottom            to the top with a constant (not always) height and get a sequence of the planar contours, each of which is represented by a sequence of the dots.
# 
# 
# These sequences of dots then, obvious, are used for a printing program along with the calculated velocities, accelerations, etc.        In order to estimate if a model fits the printerbuilding table (video)and then can be printed, our slicing software should find the optimal orientation of the model on the table, so the model will require the least possible space.
# So, in this mission you are given a list of dots, each represents a projection of a 3D model vertex onto a horizontal plane.        Your task is to find the smallest rectangle (by its area) into which all the given dots (and thus the projected contour) can be inscribed.
# 
# 
# Input:A list of tuples, each tuple contains coordinates of a projected dot (x, y). All given coordinates are integers.        Although in the example illustrations the dots are connected, forming sane contours, they can be connected in any arbitrary consequence        and that won't affect the result.
# 
# Output:The area of the smallest rectangle (with ±0.001 precision) which inscribes the given contour.
# 
# Precondition:n ∈ [3; 30] - dots numberi = range(n)xi∈ [0; 300] - x coordinate of the i-th dotyi∈ [0; 300] - y coordinate of the i-th dotthere won't be two (or more) similar dotsthere won't be a case with all the dots on the same line
# 
# 
# END_DESC

def inscribe(contour):
    # your code here

    return 0.0


if __name__ == '__main__':
    print("Example:")
    print(inscribe([(1, 1), (1, 2), (0, 2), (3, 5), (3, 4), (4, 4)]))

    def close_enough(contour, answer):
        result = inscribe(contour)
        assert abs(result - answer) <= 1e-3, \
            f'inscribe({contour}) == {answer}, and not {result}'

    # These "asserts" are used for self-checking and not for an auto-testing
    close_enough([(1, 1), (1, 2), (0, 2), (3, 5), (3, 4), (4, 4)], 6.0)
    close_enough([(6, 5), (10, 7), (2, 8)], 20.0)
    close_enough([(2, 3), (3, 8), (8, 7), (9, 2), (3, 2), (4, 4), (6, 6), (7, 3), (5, 3)], 41.538)
    close_enough([(0, 0), (0, 10), (0, 20), (100, 20), (100, 30), (120, 30), (120, 20), (120, 10), (20, 10), (20, 0)], 2679.208)
    close_enough([(10, 250), (60, 300), (300, 60), (250, 10)], 24000.0)
    close_enough([(10, 250), (60, 300), (110, 250), (160, 300), (210, 250), (160, 200), (300, 60), (250, 10)], 48000.0)
    print("Coding complete? Click 'Check' to earn cool rewards!")