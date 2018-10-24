def cesar(string,code):
        L='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        l='abcdefghijklmnopqrstuvwxyz'
        result=''
        for i in range(0,len(string)):
            Letter=string[i]
            for k in range(0, 26):
                if k+code>26 or k+code<0:
                    index=(k+code)%26
                if string[i]==L[k]:
                    Letter=L[index]
                elif string[i]==l[k]:
                    Letter=l[index]
            result=result+Letter
        return result

a=str(input())
n=input()
if type(n)!=int:
    raise TypeError('Неверный ввод данных')
cesar(a,n)
