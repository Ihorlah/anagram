# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        print(True)
    else:
        print(False)
    


#call this line of code to get result
find_anagram(word = input("type in first word: "),anagram = input ("Type in second word: "))
