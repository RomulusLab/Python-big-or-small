def is_valid(isbn):
    result = 0
    isbn_nums = isbn.replace("-", "")
    
    if len(isbn_nums) != 10:
        return False
        
    for index, char in enumerate(isbn_nums):
        if char == 'X':
            if index != 9:
                return False
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
            
        weight = 10 - index
        result += value * weight

    return result % 11 == 0