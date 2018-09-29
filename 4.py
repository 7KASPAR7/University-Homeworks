print('введите число')
a = int(input())
k = 0
for i in range(1, a):
    if a % i == 0: k = k + 1
for i in range(a,0):
    if a % i == 0: k = k + 1
if k > 2:
    print('число составное')
else:
    print('число простое')