def is_armstrong_number(number):
    digits = tuple(int(digit) for digit in str(number))
    power_of = len(digits)
    sum_of_digits = 0

    for digit in digits:
        sum_of_digits += digit ** power_of

    if sum_of_digits == number:
        return True
    return False
        
