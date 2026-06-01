def label(colors):
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]


    
    if colors[2] in color_list:
        exp = color_list.index(colors[2])
        base_value = int(str(color_list.index(colors[0])) + str(color_list.index(colors[1])))
        full_value = base_value * (10 ** exp)
        
        if full_value < 1000:
              return str(full_value) + ' ' + 'ohms'
        if 1000 <= full_value < 1000000:
            return str(int(full_value / 1000)) + ' ' + 'kiloohms'
        if 1000000 <= full_value < 1000000000:
            return str(int(full_value / 1000000)) + ' ' + 'megaohms'
        if full_value >= 1000000000:
            return str(int(full_value / 1000000000)) + ' ' + 'gigaohms'