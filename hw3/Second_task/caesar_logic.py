def encrypt(offset, text):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in range(0, len(text)):
            if text[i] in letters:
                res = res+letters[(letters.index(text[i]) + offset) % 26]
            elif text[i] in LETTERS:
                res = res + LETTERS[(LETTERS.index(text[i]) + offset) % 26]
            else:
                res = res + text[i]
    return res


def decrypt(offset, text):
    return encrypt(-offset, text)
