import numpy as np
# s= [[1,2,3,4],[5,6,7,8]]
s= [1,2,3,4]
t = [5,6,7,8]
r = [10,11,12,13]
# q= np.array(t,dtype=np.int64)   ### to show the value in the data type
q= np.array([s,t,r])
# print(q)
# print(type(q))
# print(q.ndim)
# print(q.shape)
# print(q.size)
# print(q.dtype)
# 3 dimention array

# t= np.ones((5,5),dtype=np.int64)
# t= np.zeros((5,5))
# t= np.empty((5,5))  ##give any random value in matrix
# t= np.arange(5)
# t= np.arange(5,10)
# t= np.arange(5,10,2)
# t= np.arange(5,10,0.5)
# t= np.linspace(1,10)  ## ir work on range and divied the range in equal in 50 by default
# t= np.linspace(1,10,5)  ## if 3rd parameter give it will divied them into 5 part
# t= np.linspace(1,12,12)  ## if 3rd parameter give it will divied them into 5 part
# print(t)
# s=t.reshape((4,3))
# s=t.reshape((5,1))   ### change the shape of matrix
# print(s.ravel())   ## make the matrix into 1 dim.
# print(s.sum())
# print(s.min())
# print(s.max())
# print(np.exp(s))
# print(np.sin(s))
# print(s.T)  ## in transpose the matrix 4,3 reshape one
# s.resize(3,4)  ## change the size of matrix
# print(np.random.random((5,5)))  ## create random matrix.....

# a = np.arange(15).reshape(3, 5)
# print(a.itemsize)
# print(q.sum(axis=0))   ##aboveq= np.array([s,t])
# print(q)


# print(q.std())

# print(q.mean())
# print(np.median(q))

