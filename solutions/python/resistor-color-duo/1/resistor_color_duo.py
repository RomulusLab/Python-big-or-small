def value(colors):
    resistance_values = {
        'black': str(0),
        'brown': str(1),
        'red': str(2),
        'orange': str(3),
        'yellow': str(4),
        'green': str(5),
        'blue': str(6),
        'violet':str(7),
        'grey': str(8),
        'white': str(9)
    }
    two_color_list = []
    two_color_list += [colors[0], colors[1]]
    value = ''
    
    for color in two_color_list:
        if color in resistance_values:
            value += resistance_values[color]
    return int(value)
