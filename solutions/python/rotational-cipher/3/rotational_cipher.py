def rotate(text, key):
    result = ''
    
    for char in text:
        if char.islower():
            base = ord('a')
        elif char.isupper():
            base = ord('A')
        else:
            result += char
            continue

        shifted = (ord(char) - base + key) % 26
        result += chr(shifted + base)

    return result
