def equilateral(sides):
    if len(set(sides)) <= 1 and all(num > 0 for num in sides[0:3]):
        return True
    return False


def isosceles(sides):
    sides = sorted(sides)
    if len(set(sides)) <= 2 and sides[0] + sides[1] >= sides[2]:
        return True
    return False


def scalene(sides):
    sides = sorted(sides)
    if (len(set(sides)) == 3 or len(set(sides)) == 0) and (sides[0] + sides[1] >= sides[2]):
        return True
    return False
    
