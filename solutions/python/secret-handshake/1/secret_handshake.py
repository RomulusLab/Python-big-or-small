def commands(binary_str):
    actions = ['jump', 'close your eyes', 'double blink', 'wink']
    action_bits = binary_str[1:]
    sequence = []
    
    for index in range(len(action_bits) - 1, -1, -1):
        if action_bits[index] == '1':
            sequence.append(actions[index])
    if binary_str[0] == '1':
        sequence.reverse()

    return sequence

