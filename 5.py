def pal(a):
    k=0
    a=a.lower()
    c=a.replace(' ', '')
    b=len(c)
    if b>3:
             for i in range(0,b//2-1):
                 if c[i]!=c[b-1-i]:
                     k=k+1
             if k>0:
                 print('не палиндром')
             else:
                 print('палиндром')
    else:
             if c[0]!=c[b-1]: print('не палиндром')
             else: print('палиндром')
print('Введите строку')
a=str(input())
pal(a)