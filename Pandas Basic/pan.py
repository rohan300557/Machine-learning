import pandas as pd
import numpy as np
# d = {'a':1,'b':2,'c':3,'d':4}    #### the datatype is int
# x = pd.Series(d)
# print(x)

# d = {'a':1,'b':2,'c':3,'d':4}    ####  by default the datatype is Float
# index=['a','b','c','e']
# x = pd.Series(d,index=index)
# print(x)
#
# d = {'a':'1','b':'2','c':'3','d':'4'}
# index=['a','b','d']
# x = pd.Series(d,index=index)
# print(x)

# x= np.random.random(5)
# y = pd.Series(x,index=['a','b','c','d','e'])
# print(y)

# x= np.random.random(5)
# y = pd.Series(5,index=['a','b','c','d','e'])  ## for passing Scalar value as 5
# print(y)

# d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
# print(d['a'])
# y = pd.Series(d)
# print(y['b':])
# print(y.mean())
# e = np.median(y)
# print(y[e<y])

# print(y[['a','d','f']])
# print(y[['a','d','f','h']])

# print(y.array)  ## convert to list
# print(y.to_numpy())   ### convert to array

# y = pd.Series(d)
# y['c']=12   ### change the value
# print(y)

# print(y.get('a'))
# print(y.get('x'))
# print(y.get('x',10))
# print(y.get('x',np.NAN))

# print('e' in y)
# print('r' in y)



# # print(d['a'])

# e={'a':1,'b':2,'x':3}
# z = pd.Series(e)   ###To add 2 series
# print(y+z)
# print(np.exp(y+z))
### type of any array, Find @nd highest no.
#####################################################################
# d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
# index=['a','b','d','e','f']
# q = pd.DataFrame(d , index = index )
# print(q)
#########################################################################
# s= [1,2,3]
# t = [4,5,6]
# r = [7,8,9]
# q= np.array([s,t,r])
# df = pd.DataFrame(q , index = ['a','b','c'],columns=['x','y','z'] ) #######data frame
# print(df)


d = {'Name':['sdf','fhjf','dfgd'],'Father_name':['uuu','rwddf','llll'],'M_name':['yes','math','ooo']}
df = pd.DataFrame(d,columns=['Name','Father_name','sf'])
print(df)

# d = {'Name':{'a':1,'b':2,'x':3},'Father_name':['uuu','rwddf','llll'],'M_name':['yes','math','ooo']}

# a = ['uoafv','asf','afsf','afusf']
# b = [11,22,33,44]
# x = pd.Series(a)
# y = pd.Series(b)
# q = pd.DataFrame([x,y])
# print(q)