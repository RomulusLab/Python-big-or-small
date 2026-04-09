def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    divisors = []
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    for num in range(1, number):
        if number % num == 0:
            divisors.append(num)

    if number == sum(divisors):
        return "perfect"
    if number > sum(divisors):
        return "deficient"
    if number < sum(divisors):
        return "abundant"

        
