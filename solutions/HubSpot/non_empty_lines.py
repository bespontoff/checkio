#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run non-empty-lines

# You need to count how many non-empty lines a given text has.
# 
# Empty line is a line without symbols or with only space symbols
# 
# Input:Text.
# 
# Output:Int.
# 
# 
# END_DESC

def non_empty_lines(text: str) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    print("Example:")
    print(non_empty_lines('one simple line\n'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert non_empty_lines('one simple line\n') == 1
    assert non_empty_lines('') == 0
    assert non_empty_lines('\nonly one line\n            ') == 1
    assert non_empty_lines('''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            ''') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")