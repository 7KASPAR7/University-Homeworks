
print('введите число')
a=int(input())
for i in range(1, a+1):
    if a % i == 0: print(i,-i)
for i in range(a,0):
    if a % i == 0: print(i,-i)