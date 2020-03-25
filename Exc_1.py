import numpy as np
"""
1 a)
"""
a = np.zeros(10)
a[5] = 1
print(a)
"""
1 b)
"""
b = np.arange(10,50)
print(b)
"""
1 c)
"""
c = np.arange(10)
c = c[::-1]
print(c)
"""
1 d)
"""
d = np.arange(9).reshape(3,3)
print(d)
"""
1 e)
"""
e = np.array([1,2,0,0,4,0])
e_0 = e != 0
print(e_0)
"""
1 f)
"""
f = np.random.random_sample(30)
f_mean = np.mean(f)
print(f_mean)
"""
1 g)
"""
g = np.ones(9).reshape(3,3)
g[1:-1,1:-1:] = 0
print(g)
"""
1 h)
"""
h = np.zeros((8,8), dtype= int)
h[1::2,::2]= 1
h[::2,1::2]= 1
print(h)
"""
1 i)
"""
i = np.zeros((2,2), dtype = int)
i[1::2,::2]= 1
i[::2,1::2]= 1
rep = (4,4)
i = np.tile(i, rep)
print(i)
"""
1 j)
"""
j  = np.arange(11)
j[3:8] *= -1
print(j)
"""
1 k)
"""
k = np.random.random(10)
k = np.sort(k)
print(k)
"""
1 l)
"""
l_A = np.random.randint(0,2,5)
l_B = np.random.randint(0,2,5)
equal = np.array_equal(l_A, l_B)
print(equal)
"""
1 m)
"""
m = np.arange(10, dtype=np.int32)
print(m.dtype)
m = m.astype('float32')
print(m.dtype)
"""
1 n)
"""
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = C.diagonal()
print(D)
