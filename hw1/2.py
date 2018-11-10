def calc(operand1, operation, operand2):
       if operation=='+':
           return operand1+operand2
       elif operation=='-':
           return operand1-operand2
       elif operation=='/':
           if operand2==0:
               raise ZeroDivisionError('Деление на ноль')
           else:return operand1/operand2
       elif operation=='*':
           return operand1*operand2
       else:
           raise ValueError('Неизвестная операция')
print(calc(3, '*', 80))
