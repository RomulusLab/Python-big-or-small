def rotate(text, key):
    result = ""
    
    for char in text:
        if char.isalpha() and char.islower():
            convert_ascii = ord(char)
            new_num = (convert_ascii - ord('a') + key) % 26
            new_char = chr(new_num + ord('a'))
            result += new_char
        elif char.isalpha() and char.isupper():
            convert_ascii = ord(char)
            new_num = (convert_ascii - ord('A') + key) % 26
            new_char = chr(new_num + ord('A'))
            result += new_char
        else:
            result += char

    return result
