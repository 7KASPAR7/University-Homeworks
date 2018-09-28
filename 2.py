def calc(a, b, c):
       if b=='+':
           return a+c
       elif b=='-':
           return a-c
       elif b=='/':
           return a/c
       elif b=='*':
           return a*c
       else:
           raise ValueError('Неизвестная операция')
print(calc(5, '*', 3))
