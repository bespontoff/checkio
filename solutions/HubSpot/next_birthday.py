#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run next-birthday

# You have to write a function that receives a "today" date and a dictionary of family birthdates,    and for the person(s) whose birthday is next (today or later),    return the number of days between "today" and that birthday, and the age they will be.
# 
# Note about leap days:If someone is born on February 29th, then he or she will    celebrate birthdays on March 1st when necessary.
# 
# Input:Two arguments:a tuple of three integers (year, month, day) representing a date;a dictionary: keys are string and values are dates.Output:An integer and a dictionary (keys are string and values are integers).
# 
# 
# END_DESC

from typing import Dict, Tuple

Date = Tuple[int, int, int]


def next_birthday(today: Date, birthdates: Dict[str, Date]) -> Tuple[int, Dict[str, int]]:
    ...


if __name__ == '__main__':
    FAMILY = {
        'Brian': (1967, 5, 31),
        'Léna': (1970, 10, 3),
        'Philippe': (1991, 6, 15),
        'Yasmine': (1996, 2, 29),
        'Emma': (2000, 12, 25),
    }

    TESTS = [
        ((2020, 9, 8), (25, {'Léna': 50})),
        ((2021, 10, 4), (82, {'Emma': 21})),
        ((2022, 3, 1), (0, {'Yasmine': 26})),
    ]

    for nb, (day, answer) in enumerate(TESTS, 1):
        user_result = tuple(next_birthday(day, FAMILY.copy()))
        if user_result != answer:
            print(f'You failed the test #{nb}.')
            print(f'Your result: {user_result}')
            print(f'Right result: {answer}')
            break
    else:
        print('Well done! Click on "Check" for real tests.')