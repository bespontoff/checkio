#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run stressful-subject

# 
# END_DESC

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    from string import digits, punctuation, whitespace
    import itertools

    stress = ["help", "asap", "urgent"]

    if subj.endswith('!!!') or subj.isupper(): return True
    subj = ''.join([ch.lower() for ch, _ in itertools.groupby(subj) if ch not in punctuation and ch not in digits and ch not in whitespace])

    for word in stress:
        if word in subj: return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')