def prost(a):
    result=[]
    b=abs(a)
    while b>=1:
        if a%b==0:
            result.append(b)
        b=b-1
    lst=[-x for x in result]
    result.extend(lst)
    if len(result)==4:
        print('Простое число')
    else:
        print('Составное число')
print('Введите число')
c=int(input())
prost(c)

