import random
import numpy as np
import numpy.linalg as la


def solve_upper_triang(A, b):
    """
    solves Ax=b for U-triangular A
    """
    A = np.array(A, ndmin=2)
    b = np.reshape(b, (-1, 1))
    n = len(b)

    Ab = np.concatenate((A, b), axis=1)

    for i in range(n)[::-1]:
        Ab[i, :] /= Ab[i, i]
        for j in range(i):
            Ab[j, :] -= Ab[i, :] * Ab[j, i]

    A, b = np.split(Ab, [n], axis=1)
    return b.reshape(-1)


def solve_lower_triang(A, b):
    """
    solves Ax=b for L-triangular A
    """
    A = np.array(A, ndmin=2)
    b = np.reshape(b, (-1, 1))
    n = len(b)

    Ab = np.concatenate((A, b), axis=1)

    for i in range(n):
        Ab[i, :] /= Ab[i, i]
        for j in range(i + 1, n):
            Ab[j, :] -= Ab[i, :] * Ab[j, i]
    A, b = np.split(Ab, [n], axis=1)
    return b.reshape(-1)


def lu(A):
    """
    LU decomposition
    """
    LU = np.matrix(np.zeros([A.shape[0], A.shape[1]]))
    n = A.shape[0]
    for k in range(n):
        for j in range(k, n):
            LU[k, j] = A[k, j] - LU[k, :k] * LU[:k, j]
        for i in range(k + 1, n):
            LU[i, k] = (A[i, k] - LU[i, : k] * LU[: k, k]) / LU[k, k]
    L = LU.copy()
    U = LU.copy()
    for i in range(L.shape[0]):
        L[i, i] = 1
        L[i, i + 1:] = 0
    for i in range(1, U.shape[0]):
        U[i, :i] = 0
    return L, U

def generate_form():
    N = 7
    Matrix = np.random.randint(-100, 100, (N, N))
    # print(Matrix)
    A = np.dot(Matrix, np.transpose(Matrix)) / 1000
    # NormA = np.la.norm(A)
    b = np.random.randint(-100, 100, (N, 1)) / 10
    # Normb = np.la.norm(b)
    print('A:', A, '\n', 'b:', b)
    return A, b

def solve_lu(A, b):
    """
    solve Ax=b using LU decomposition
    """
    L, U = lu(A)
    b1 = solve_lower_triang(L, b)
    return solve_upper_triang(U, b1)

def transform(A, b):
    """
    Ax = b -> x = Cx+d
    """
    C = A.copy()
    d = b.copy()
    for i in range(len(C)):
        d[i] /= C[i, i]
        C[i, :] /= -C[i, i]
        C[i, i] = 0
    return C, d

def seidel(A, b, tol):
    """
    Gauss-Seidel method
    returns: list of x, list of y
    """
    n = len(A)
    C, d = transform(A, b)
    x = np.copy(d)
    xs = []
    errors = []
    max_iterations = 10000
    # print(x ,'CCC',C[1][:] @ x,'DDD', C[1][:] @ x)
    for k in range(max_iterations):
        for i in range(n):
            x[i] = C[i][:] @ x + d[i]
        err = np.linalg.norm(A @ x - b)
        errors.append(err)
        if err <= tol:
            return x.reshape(-1), k, err
    xs.append(x)
    return x.reshape(-1), k, err

def gradient(A, b, tol):
    x = np.copy(b)
    for i in range(10000):
        q = A @ x + b
        u = - (q.reshape(-1) @ (A @ x + b) / (q.reshape(-1) @ A @ q))
        x1 = x + u * q
        err = np.linalg.norm(x1 - x)
        x = x1
        if err <= tol:
            return x.reshape(-1), i, err
    return x.reshape(-1), i, err

def coordinates(A, b, tol):
    x = np.copy(b)
    q = np.zeros((len(A), 1))
    x1 = x
    for i in range(10000):
        k = i % len(A)
        q[k, 0] = 1
        u = -(q.reshape(-1) @ (A @ x1 + b)) / (A[k, k])
        x1 = x1 + u * q
        if (k == 0):
            err = np.linalg.norm(x1 - x)
            if err <= tol:
                return x.reshape(-1), i // 7, err
            x = x1
        q[k, 0] = 0
    return x.reshape(-1), i // 7, err

A, b = generate_form()
#x = solve_lu(A, -b)
y, iterations, err = seidel(A, -b, 1e-6)
#print('LU:', x)
print('Seidel:', y, '\n', 'Iterations:', iterations, '\n', 'err:', err)
z, k, err = gradient(A, b, 1e-6)
print('Gradient:', z, '\n', 'Iterations:', k, '\n', 'err:', err)
z, k, err = coordinates(A, b, 1e-6)
print('Coordinates:', z, '\n', 'Iterations:', k, '\n', 'err:', err)






