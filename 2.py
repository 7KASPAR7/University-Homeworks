def calc(operand1, operation, operand2):
       if operation=='+':
           return operand1+operand2
       elif operation=='-':
           return operand1-operand2
       elif operation=='/':
           return operand1/operand2
       elif operation=='*':
           return operand1*operand2
       else:
           raise ValueError('Неизвестная операция')
print(calc(5, '*', 3))
