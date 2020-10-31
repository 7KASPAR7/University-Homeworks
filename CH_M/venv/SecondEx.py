import math
import numpy as np
import matplotlib.pyplot as plt

def calc_function(x):
    result = 1/math.tan(x/2 + math.pi/2) + x**2 + 1
    return result


def function_plot(X):
    print(X)
    Y = []
    for x in X:
        func = calc_function(x)
        Y.append(func)
    plt.plot(X, Y, label = 'f')

def equidistant(X):
    E = []
    step = 0.5
    Z = abscess_function(X[0], step)
    print(Z)
    Y = []
    for point in X:
        Pn = 0
        for x in Z:
            lk = multiplier(point, x, Z)
            Pn += lk*calc_function(x)
        Y.append(Pn)
        if (X.index(point)%10 == 0):
            error = abs(calc_function(point) - Pn)
            E.append(error)
    print('errors: ', E)
    print('max error: ', max(E))
    plt.plot(X, Y, label = 'Eq')

def multiplier(point, k, Z):
    lk = 1
    for x in Z:
        if (x != k):
            lk = lk * (point-x) / (k-x)
    return lk

def abscess_function(point, step):
    s = point
    X = []
    while (s <= -point):
        X.append(s)
        s += step
    if (-point not in X):
        X.append(-point)
    return X

def Chebyshev(X):
    E = []
    N = 13
    Z = []
    for i in range(0, N):
        z = 1/2*(X[-1]-X[0])*math.cos(((2*i+1)*math.pi)/(2*N)) + (X[-1] + X[0])
        Z.append(z)
    print(Z)
    Y = []
    for point in X:
        Pn = 0
        for x in Z:
            lk = multiplier(point, x, Z)
            Pn += lk * calc_function(x)
        Y.append(Pn)
        if (X.index(point)%10 == 0):
            error = abs(calc_function(point) - Pn)
            E.append(error)
    print('errors: ', E)
    print('max error: ', max(E))
    plt.plot(X, Y, label = 'Ch')


point = -1
step = 0.01
X = abscess_function(point, step)
function_plot(X)
equidistant(X)
Chebyshev(X)
plt.legend()
plt.show()