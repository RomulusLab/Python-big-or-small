def is_pangram(sentence):
    letters = {character for character in sentence.lower() if character.isalpha()}
    return len(letters) == 26
