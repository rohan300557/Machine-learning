import pandas as pd

df2 = pd.read_csv('user.txt',sep='|')
# print(df2)

# # Q 6.
# age = df2.groupby('occupation').mean()
# print(age['age'])
### todo:- ---------- OR ------
# print(df2.groupby('occupation')['age'].mean())

# # Q 7.
# age1 = df2.groupby('occupation').min()
# age2 = df2.groupby('occupation').max()
# age = pd.concat([age1['age'],age2['age']],axis=1)
# col = ['min','max']
# age.columns= col
# print(age)

# # Q 8.
# print(df2.groupby(['occupation','gender'])['age'].mean())