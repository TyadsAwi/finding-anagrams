# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(str1, str2):
    a = str1.lower()
    b = str2.lower()
    if sorted(a.replace(" ", "")) == sorted(b.replace(" ", "")):
        return True
    else:
        return False

