#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run weekly-calendar

# Let's make a weekly calendar.
# 
# You are given four integers as input values. (A year, month, day and the first day of the week [0: Monday...6: Sunday])
# You must return a list (or an iterable) of the week that includes the date in the input values.
# This begins with the first day of the week.
# 
# 
# END_DESC

from typing import List


def weekly_calendar(year: int, month: int, day: int, firstweekday: int) -> List[int]:
    # your code here
    return []


if __name__ == '__main__':
    print("Example:")
    print(list(weekly_calendar(2020, 1, 1, 0)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(weekly_calendar(2020, 1, 1, 0)) == [30, 31, 1, 2, 3, 4, 5], "01/01/2020 Monday"
    assert list(weekly_calendar(2020, 9, 20, 6)) == [20, 21, 22, 23, 24, 25, 26], "09/20/2020 Sunday"
    assert list(weekly_calendar(2020, 9, 30, 0)) == [28, 29, 30, 1, 2, 3, 4], "09/30/2020 Monday"
    assert list(weekly_calendar(2020, 2, 29, 2)) == [26, 27, 28, 29, 1, 2, 3], "02/29/2020 Wednesday"
    print("Coding complete? Click 'Check' to earn cool rewards!")