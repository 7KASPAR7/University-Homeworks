def deli(a):
    result=[]
    b=abs(a)
    while b>=1:
        if a%b==0:
            result.append(b)
        b=b-1
    lst=[-x for x in result]
    result.extend(lst)
    return(result)
print(deli(777))
