def rotate(lst):
    if lst==[]:
        return lst
    else:
        result=[]
        k=lst[-1]
        for el in lst:
            result.append(el)
        result.insert(0,k)
        result.pop(-1)
        return result
l=[1,2,3,4,5,6]
print(rotate(l))
print(l)