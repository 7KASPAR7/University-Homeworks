def encrypt(offset, text):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(0, len(text)):
        symbol = text[i]
        for k in range(0, 26):
            index = (k + offset) % 26
            if text[i] == LETTERS[k]:
                symbol = LETTERS[index]
            elif text[i] == letters[k]:
                symbol = letters[index]
        result = result + symbol
    return result


def decrypt(offset, text):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(0, len(text)):
        symbol = text[i]
        for k in range(0, 26):
            index = (k - offset) % 26
            if text[i] == LETTERS[k]:
                symbol = LETTERS[index]
            elif text[i] == letters[k]:
                symbol = letters[index]
        result = result + symbol
    return result
