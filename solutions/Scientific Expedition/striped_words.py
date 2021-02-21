#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run striped-words

# Our robots are always working to improve their linguistic skills.    For this mission, they research the Latin alphabet and its applications.
# 
# The alphabet contains both vowel and consonant letters (yes, we divide the letters).
# Vowels --A E I O U Y
# Consonants --B C D F G H J K L M N P Q R S T V W X Z
# 
# You are given a block of text with different words.     These words are separated by whitespaces and punctuation marks.    Numbers are not considered as words in this mission (a mix of letters and digits is not a word either).    You should count the number of words (striped words) where the vowels with consonants are alternating;     words that you count cannot have two consecutive vowels or consonants.    The words consisting of a single letter are not striped -- don't count those. Casing is not significant for this mission.
# 
# Input:A text as a string (unicode)
# 
# Output:A quantity of striped words as an integer.
# 
# Precondition:The text contains only ASCII symbols.
# 0 < len(text) < 105
# 
# 
# END_DESC

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper()    
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    text = text.replace('?', ' ')
    text = text.replace('!', ' ')
    text = text.split()     
    count = 0
    print(text)
    
    def polos(word):
        
        if len(word) <= 1: return False
        if len(word) == 2:
            if word[0] in VOWELS and word[1] in CONSONANTS: return True
            elif word[0] in CONSONANTS and word[1] in VOWELS: return True
            else: return False
        
        nechet = word[::2]
        chet = word[1::2]        
        print(nechet, chet)
        if nechet[0] in VOWELS:
            
            for char in nechet:
                if char not in VOWELS:
                    return False
            for char in chet:
                if char not in CONSONANTS:
                    return False
        
        elif nechet[0] in CONSONANTS:            
            for char in nechet:
                if char not in CONSONANTS:                    
                    return False
            for char in chet:                
                if char not in VOWELS:                    
                    return False            
        elif nechet[0].isdigit(): return False
        return True
    
    for word in text:
        if polos(word):
            count += 1
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("1st 2a ab3er root rate") == 1, "Only of2"