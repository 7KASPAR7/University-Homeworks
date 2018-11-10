def List(s):
    result = []
    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == ')' or s[i] == '[':
            result.append(s[i])
        elif s[i] == ']' or s[i] == '{' or s[i] == '}':
            result.append(s[i])
    return result


def proverka(s):
    for i in range(1, len(s)):
        sum = s[i - 1] + s[i]
        if sum == '()' or sum == '[]' or sum == '{}':
            s[i] = ' '
            s[i - 1] = ' '
    result = []
    for i in range(0, len(s)):
        if s[i] != ' ':
            result.append(s[i])
    return result


def redactor(s):
    while len(s) != len(proverka(s)):
        s = proverka(s)
    return s


def check(string):
    LST = ['(', ')', '{', '}', '[', ']']
    k = True
    for i in LST:
        if i in string:
            k = False
            break
    return k


def program(string):
    return check(redactor(List(string)))
