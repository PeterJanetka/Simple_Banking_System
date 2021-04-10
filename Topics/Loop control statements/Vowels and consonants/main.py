for char in input():
    if char.isalpha() is False:
        break
    else:
        if char in "aeiou":
            print("vowel")
        else:
            print("consonant")
