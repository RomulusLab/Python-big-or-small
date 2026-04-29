def is_isogram(string):
    letters_only = [character for character in string.lower() if character.isalpha()]
    
    for letter in letters_only:
        if letters_only.count(letter) > 1:
            return False
    return True
