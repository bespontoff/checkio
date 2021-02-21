#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run workout

# Sam has prepared a fitness program so that he can become stronger! 	The program is made of N sessions. During the i-th session, Sam will 	do a certain amount of pushups. The number of pushups he does in each 	session is strictly increasing.
# 
# Thedifficultyof his fitness program is equal to the maximum 	difference in the number of pushups between any two consecutive training 	sessions.
# 
# To make his program less difficult, Sam has decided to add up to K 	additional training sessions to his fitness program. He can add these 	sessions anywhere in his fitness program, and do any number of pushups 	in each of them. After the additional training sessions are added, 	the number of pushups he does in each session must still be strictly increasing. 	What is the minimum possible difficulty?
# 
# This mission was proposed by Yossi Matsumoto and Wajeb Saab for Google Kickstart Round A 2020.
# 
# Input:Two argumentsthe first one is a list of positive integers - the number of pushups in			each training session;the second is a positive integer - additional sessions that Sam may 			add to his fitness program.
# 
# 
# 
# Output:An integer - the minimum difficulty possible after up to K 		additional training sessions are added.
# 
# 
# 
# Precondition:2 ≤ N ≤ 10001 ≤ K ≤ 500
# 
# 
# END_DESC

from typing import List

def workout(sessions: List[int], additional: int) -> int:
    # your code here
    return 1


if __name__ == '__main__':
    print("Example:")
    print(workout([100, 200, 230], 1))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert workout([100, 200, 230], 1) == 50,     "First"
    assert workout([10, 13, 15, 16, 17], 2) == 2, "Second"
    assert workout([9, 10, 20, 26, 30], 6) == 3,  "Third"
    print("Coding complete? Click 'Check' to earn cool rewards!")