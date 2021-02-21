#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run mind-switcher

# - Oh no! Is it possible to get everyone back to normal using four or more bodies?
# 
# - I'm not sure. I'm afraid we need to use...MATH.
# 
# "Futurama" - Season 6 Episode 10 - "The Prisoner of            Benda"
# 
# Sophia's drones are simple robots which do dangerous work.    Just in case one breaks, Sophia has a backup machine for these drones.    This machine can copy a robots mind and has a secret and undocumented function.    The backup machine can also operate as a mind switcher for robots.
# 
# Sophia forgot to turn off the machine and left the drones in the same room.    When she had returned some drones already swapped their minds with each other.    We should help them to return to their original bodies as their current state voids the manufacturer warranty.
# 
# We have a log from the machine, of which drones minds were swapped.    There is however one slight problem - no pair of bodies can swap minds more than once.    However, with two additional bodies we can return the switching chaos back to a normal state of things.    Nikola and Sophia have offered to help us ("nikola" and "sophia").
# 
# You are given an array with with information about the recent swaps.    Each entry is a set with two names of robots (bodies).    You can operate with bodies which were written in the journal and with two additional bodies - "nikola" and    "sophia".    Find the sequence of the swaps required to return all minds to their original bodies.    The result should be represented as a list/tuple of sets with two names in each.
# 
# Input:A journal as a tuple of sets. Each set contains two strings.
# 
# Output:The sequence of actions as a list/tuple of sets. Each set contains two strings.
# 
# Precondition:
# 0 < len(journal) ≤ 55
# Journalis correct.
# 
# Sources:Cohen, David (2010). Futurama volume 5 DVD episode 10 "The Prisoner of Benda" (DVD). 20th Century Fox.
# 
# 
# END_DESC

def mind_switcher(journal):
    return ()


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(func, data):
        robots = {"nikola": "nikola", "sophia": "sophia"}
        switched = []
        for pair in data:
            switched.append(set(pair))
            r1, r2 = pair
            robots[r1], robots[r2] = robots.get(r2, r2), robots.get(r1, r1)

        result = func(data)
        if not isinstance(result, (list, tuple)) or not all(isinstance(p, set) for p in result):
            print("The result should be a list/tuple of sets.")
            return False
        for pair in result:
            if len(pair) != 2:
                print(1, "Each pair should contain exactly two names.")
                return False
            r1, r2 = pair
            if not isinstance(r1, str) or not isinstance(r2, str):
                print("Names must be strings.")
                return False
            if r1 not in robots.keys():
                print("I don't know '{}'.".format(r1))
                return False
            if r2 not in robots.keys():
                print("I don't know '{}'.".format(r2))
                return False
            if set(pair) in switched:
                print("'{}' and '{}' already were switched.".format(r1, r2))
                return False
            switched.append(set(pair))
            robots[r1], robots[r2] = robots[r2], robots[r1]
        for body, mind in robots.items():
            if body != mind:
                print("'{}' has '{}' mind.".format(body, mind))
                return False
        return True

    assert check_solution(mind_switcher, ({"scout", "super"},))
    assert check_solution(mind_switcher, ({'hater', 'scout'}, {'planer', 'hater'}))
    assert check_solution(mind_switcher, ({'scout', 'driller'}, {'scout', 'lister'},
                                          {'hater', 'digger'}, {'planer', 'lister'}, {'super', 'melter'}))