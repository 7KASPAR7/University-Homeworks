def cesar(string, code):
        LETTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letter = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        for i in range(0, len(string)):
            symbol = string[i]
            for k in range(0, 26):
                if k+code > 26 or k+code < 0:
                    index = (k+code) % 26
                if string[i] == LETTER[k]:
                    symbol = LETTER[index]
                elif string[i] == letter[k]:
                    symbol = letter[index]
            result = result+symbol
        return result


a = str(input())
n = input()
if type(n) != int:
    raise TypeError('Неверный ввод данных')
cesar(a, n)
