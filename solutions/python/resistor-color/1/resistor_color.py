resistance_value = {
    'black': 0, 
    'brown': 1, 
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def color_code(color):
    if color in resistance_value:
        return resistance_value[color]


def colors():
    color_list = [*resistance_value]
    return color_list
