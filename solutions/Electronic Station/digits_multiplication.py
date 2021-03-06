#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run digits-multiplication

# You are given a positive integer.    Your function should calculate the product of the digits excluding any zeroes.
# 
# For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
# 
# Input:A positive integer.
# 
# Output:The product of the digits as an integer.
# 
# Precondition:0 < number < 106
# 
# 
# END_DESC

def checkio(number):
    s = str(number)
    res = 1
    for n in s:
       if int(n) != 0: 
           res *= int(n)
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1