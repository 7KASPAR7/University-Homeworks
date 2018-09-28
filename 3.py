print('введите число')
a=int(input())
print(1,-1)
for i in range(2,a):
    if a%i==0: print(i, -i)
print(a,-a)