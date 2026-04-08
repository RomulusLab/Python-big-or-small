def score(x, y):
    distance = (x**2 + y**2) ** 0.5 # Euclidean formula

    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0
    
