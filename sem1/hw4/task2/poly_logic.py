def derivative(string):
    lst = ['+', '-']
    koef = 0
    step = 0
    result = res(string)
    for i in range(0, len(string)-1):
        if string[i] in lst:
            koef = find_koef(string, i)
        elif string[i]+string[i+1] == 'x^':
            step, sign = find_step(string, i+1, lst)
        elif string[i]+string[i+1] == 'x+' or string[i]+string[i+1] == 'x-':
            step = '1'
            sign = '+'
        if koef != 0 and step != 0:
                divkoef = int(koef) * int(step)
                divstep = int(step) - 1
                if step == '2':
                    result = result + str(divkoef) + 'x' + sign
                elif step == '1':
                    result = result + str(koef) + sign
                else:
                    result = result + str(divkoef) + 'x^' + str(divstep) + sign
                koef = 0
                step = 0
    if result[0:len(result) - 1] == '':
        return '0'
    else:
        return result[0:len(result) - 1]


def find_step(string, index, lst):
    for l in range(index, len(string)):
        if string[l] in lst:
            return string[index + 1:l], string[l]


def find_koef(string, index):
    for l in range(index, len(string)):
        if string[l] == 'x' or string[l] == '*':
            if string[index + 1:l] == '':
                return 1
            else:
                return string[index+1:l]


def redactor(string):
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
    return derivative(redactor(string))
