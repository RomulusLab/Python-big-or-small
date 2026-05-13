def value(colors):
    resistance_values = {
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
    
    value = ''
    
    for color in colors[:2]:
        if color in resistance_values:
            value += str(resistance_values[color])
    return int(value)
