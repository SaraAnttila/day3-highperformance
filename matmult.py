# Program to multiply two matrices using nested loops
#import random
import numpy as np

N = 250

# NxN matrix

# X = []
# for i in range(N):
#     x_i = []
#     for r in range(N):
#         x = random.randint(0,100)
#         x_i.append(x)
#     X.append(x_i)
#     #X.append([random.randint(0,100) for r in range(N)])
#
# # Nx(N+1) matrix
#
# Y = []
# for i in range(N):
#     y_i = []
#     for r in range(N+1):
#         y = random.randint(0,100)
#         y_i.append(y)
#     Y.append(y_i)
#     #Y.append([random.randint(0,100) for r in range(N+1)])
#
# # result is Nx(N+1)
# result = []
# for i in range(N):
#     result.append([0] * (N+1))
#
#
#
#
# # iterate through rows of X
# for i in range(len(X)):
#     # iterate through columns of Y
#     for j in range(len(Y[0])):
#         # iterate through rows of Y
#         for k in range(len(Y)):
#             result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#     print(r)

A = np.random.random((N,N))
B = np.random.random((N,N+1))
result2 = np.matmul(A,B)

print(np.array_equal(result, result2))
