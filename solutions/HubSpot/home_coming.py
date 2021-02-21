#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run home-coming

# Jessica is going to see her family overseas today, so she goes	to the local gift shop to buy some souvenirs. There areNsouvenirs	on the shelf, numbered 1, 2, ...,Nfrom left to right. Souvenirs come 	in different types, which are denoted by positive integers. Jessica is 	in a hurry, so she can take only a consecutive interval of souvenirs. 	Formally, Jessica selects two indices,landr, and takes 	all of the souvenirs numberedl, l+1, ..., r-1, r. Also, due to 	tax rules, airport security will throw away all souvenirs of a particular type if 	Jessica has more thanSof that type in the chosen interval.
# 
# For example, supposeS= 2, and Jessica brings six souvenirs: one of type 0, 	two of type 1, and three of type 2. She will be allowed to keep the souvenir of type 0 and both 	souvenirs of type 1, but she will lose all of the souvenirs of type 2!
# 
# Jessica needs to chooselandrsuch that she can take the maximum 	number of souvenirs for her family. What is the maximum number of souvenirs she can bring?
# 
# This mission was proposed by Himanshu Jaju and Sadia Nahreen for Google Kickstart Round B 2019.
# 
# Input:Two arguments:a list of positive integers, which represents the types of souvenirs on the shelf from left to right;a positive integer, the maximum amount of souvenirs of a single type in the chosen interval.
# 
# 
# 
# Output:An integer, the maximum number of souvenirs Jessica can bring to her family.
# 
# 
# 
# Precondition:2 ≤N≤ 10001 ≤S≤ 100
# 
# 
# END_DESC

from typing import List

def home_coming(souvenirs: List[int], s: int) -> int:
    # your code here
    return 1


if __name__ == '__main__':
    print("Example:")
    print(home_coming([1, 1, 4, 1, 4, 4], 2))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert home_coming([1, 1, 4, 1, 4, 4], 2) == 4,             "Example #1"
    assert home_coming([1, 2, 5, 3, 4, 5, 6, 7], 1) == 6,       "Example #2"
    assert home_coming([1, 2, 8, 8, 8, 8, 8, 3, 4, 1], 1) == 4, "Example #3"
    print("Coding complete? Click 'Check' to earn cool rewards!")