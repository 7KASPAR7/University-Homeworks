def proizvodnaya(string):
    lst = ['+', '-']
    a = 0
    b = 0
    result = res(string)
    for i in range(0, len(string)-1):
        if string[i] in lst:
            a = koef(string, i)
        elif string[i]+string[i+1] == 'x^':
            b, z = step(string, i+1, lst)
        elif string[i]+string[i+1] == 'x+' or string[i]+string[i+1] == 'x-':
            b = '1'
            z = '+'
        if a != 0 and b != 0:
                k = int(a) * int(b)
                s = int(b) - 1
                if b == '2':
                    result = result + str(k) + 'x' + z
                elif b == '1':
                    result = result + str(a) + z
                else:
                    result = result + str(k) + 'x^' + str(s) + z
                a = 0
                b = 0
    if result[0:len(result) - 1] == '':
        return '0'
    else:
        return result[0:len(result) - 1]


def step(string, i, lst):
    for l in range(i, len(string)):
        if string[l] in lst:
            return string[i + 1:l], string[l]


def koef(string, i):
    for l in range(i, len(string)):
        if string[l] == 'x' or string[l] == '*':
            if string[i + 1:l] == '':
                return 1
            else:
                return string[i+1:l]


def obrabotka(string):
    string = string.replace(' ', '')
    string = string.lower()
    if string[0] != '-':
        string = '+' + string
    result = string + '+'
    return result


def res(string):
    if string[0] == '-':
        result = '-'
    else:
        result = ''
    return result


def program(string):
    return proizvodnaya(obrabotka(string))
