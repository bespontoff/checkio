#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run house-password

# 
# END_DESC

def checkio(data):
    less10 = True
    onedig = False
    uplet = False
    downlet = False
    if len(data) < 10: less10 = False
    for ch in data:
        if ch.isdigit(): onedig = True
        if ch.isalpha() and ch.isupper(): uplet = True
        if ch.isalpha() and ch.islower(): downlet = True
    
    if less10 and onedig and uplet and downlet: return True
    else: return False    

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"