def resistor_label(colors):
    color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    
    tolerance_dict = {'grey': '±0.05%', 'violet': '±0.1%', 'blue': '±0.25%', 'green': '±0.5%', 'brown': '±1%', 'red': '±2%', 'gold': '±5%', 'silver': '±10%'}
    
    if len(colors) == 4:
        exp = color_list.index(colors[2])
        base_value = int(str(color_list.index(colors[0])) + str(color_list.index(colors[1])))
        full_value = base_value * (10 ** exp)
    if len(colors) == 5:
        exp = color_list.index(colors[-2])
        base_value = ''
        for color in colors[:3]:
            base_value += str(color_list.index(color))
        base_value = int(base_value)
        full_value = base_value * (10 ** exp)
    if len(colors) < 4:
        full_value = color_list.index(colors[-1])
        return f"{full_value} ohms"
        
   
    tolerance = tolerance_dict.get(colors[-1], "")

    if full_value < 1000:
        scaled = full_value / 1
        if scaled.is_integer():
            scaled = int(scaled)
        magnitude = 'ohms'
    if 1000 <= full_value < 1000000:
        scaled = full_value / 1000
        if scaled.is_integer():
            scaled = int(scaled)
        magnitude = 'kiloohms'
    if 1000000 <= full_value < 1000000000:
        scaled = full_value / 1000000
        if scaled.is_integer():
            scaled = int(scaled)
        magnitude = 'megaohms'
    if full_value >= 1000000000:
        scaled = full_value / 1000000000
        if scaled.is_integer():
            scaled = int(scaled)
        magnitude = 'gigaohms'

    return f"{scaled} {magnitude} {tolerance}"
    
    