#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run family-dinner

# Dr. Mickhead's family is visiting him next Sunday to have dinner together. He wishes the party to be really special, so he plans to use his best plates for the table setting. Dr. Mickhead has N stacks of plates. Each stack contains K plates. Each plate has a positive beauty value, describing how beautiful it looks. Dr. Mickhead would like to take exactly P plates to use for dinner. If he would like to take a plate from a stack, he must also take all of the plates above it.Help Dr. Mickhead to calculate the maximum total sum of beauty values that canbe achieved by picking P plates.
# 
# Note:P is always less than or equal to the total amount of plates in all stacks.This mission was proposed by Ben Jacobson and Wajeb Saab for Google Kickstart Round A 2020.
# 
# Input:Two argumentsThe first one is a list of lists of equal size. The i-th list contains positive integers, 			describing the beauty values of i-th stack of plates from top to bottom;The second is a positive integer. The amount of plates Dr. Mickhead is willing to put			on the table.
# 
# 
# 
# Output:An integer - the maximum total sum of beauty values that can be achieved 	with respect to the constraints.
# 
# Precondition:1 ≤ len(stacks) ≤ 1001 ≤ len(stacks[i]) ≤ 501 ≤ stacks[i][j] ≤ 200
# 
# 
# END_DESC

from typing import List

def best_plates(stacks: List[List[int]], guests: int) -> int:
    #replace this for solution
    return 1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    print("Example:")
	
    print(best_plates([[10, 10, 100, 30], [80, 50, 10, 50,]], 5))

    assert best_plates([[10, 10, 100, 30], 
						[80, 50, 10, 50,]], 5) == 250, "Example #1"
						
    assert best_plates([[80, 80],
						[15, 50],
						[20, 10]], 3) == 180, "Example #2"
						
    print("Coding complete? Click 'Check' to earn cool rewards!")