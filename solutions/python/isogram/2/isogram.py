def is_isogram(string):
    dupes = set()
    
    for char in string.lower():
        if char.isalpha():
            if char in dupes:
                return False
            dupes.add(char)
    return True
