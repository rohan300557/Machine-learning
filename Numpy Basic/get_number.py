import numpy as np
# s= [[1,2,3,4],[5,6,7,8]]
# s= [1,2,3,4]
# t = [5,6,7,8]
# r = [9,10,11,12]
# q= np.array([s,t,r])
# # print(q[2,1])
# print(q.flat)
# print(q[:,0])
# print(q[1,1:])
# print(q[[1,2],1:])
# print(q[:2,:2])

############################## mean,median,stadard deviation matrix each element

# print(np.std(q))
# print(q.mean())
# print(np.median(q))

# for x in np.nditer(q):
#     print(x, end=' ')

# for x in q.flat:    ##### itrate every element in matrix
#     print(x)



# print(q<5)  ###give true for below 5  and false for above
# print(q[q<5])   ### give the no below the 5
# print(q[q%2==0])   ######### to get even no. in the matrix




# s= [4,2,3]
# t = [5,2,4]
# print(np.intersect1d(s,t))

# r = [3,5,4]
# q= np.array([s,t])
# print(np.repeat(s,t))
# print(np.unique([q]))    ### remove duplicate


