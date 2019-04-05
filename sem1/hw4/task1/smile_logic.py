def List(string):
    result = []
    for i in range(0, len(string)):
        if string[i] == '(' or string[i] == ')' or string[i] == '[':
            result.append(string[i])
        elif string[i] == ']' or string[i] == '{' or string[i] == '}':
            result.append(string[i])
    return result


def proverka(string):
    for i in range(1, len(string)):
        sum = string[i - 1] + string[i]
        if sum == '()' or sum == '[]' or sum == '{}':
            string[i] = ' '
            string[i - 1] = ' '
    result = []
    for i in range(0, len(string)):
        if string[i] != ' ':
            result.append(string[i])
    return result


def redactor(string):
    while len(string) != len(proverka(string)):
        string = proverka(string)
    return string


def check(string):
    LST = ['(', ')', '{', '}', '[', ']']
    k = True
    for symbol in LST:
        if symbol in string:
            k = False
            break
    return k


def program(string):
    return check(redactor(List(string)))
