def pal(str):
    k=0
    str=str.lower()
    STR=str.replace(' ', '')
    length=len(STR)
    if length>3:
             for i in range(0,length//2-1):
                 if STR[i]!=STR[length-1-i]:
                     k=k+1
             if k>0:
                 print('не палиндром')
             else:
                 print('палиндром')
    else:
             if STR[0]!=STR[length-1]: print('не палиндром')
             else: print('палиндром')
print('Введите строку')
S=str(input())
pal(S)