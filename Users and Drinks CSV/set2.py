import pandas as pd

################33333### todo:-  drinks.csv

df = pd.read_csv("drinks.csv")
# print(df)
df.dropna( inplace=True)


# # Q 1.
# lis=[]
# for a in df['continent']:
#     if a not in lis:
#         lis.append(a)
# lis.sort()
# dic={}
# for a in lis:
#     print(a,"{:.6f}".format(df['beer_servings'][df['continent']==a].mean()))
###todo:------- OR  ----------
# print(df.groupby('continent')['beer_servings'].mean())

# # Q 2.
# print(df.groupby('continent').mean())

# # Q 3.
# print(df.groupby('continent')['wine_servings'].describe())

# # Q 4.
# print(df.groupby('continent').median())

# # Q 5.
# lis=[]
# for a in df['continent']:
#     if a not in lis:
#         lis.append(a)
# lis.sort()
# Mean=[]
# Max=[]
# Min=[]
# dic={}
# for a in lis:
#     Mean.append("{:.6f}".format(df['spirit_servings'][df['continent']==a].mean()))
#     Max.append(int(df['spirit_servings'][df['continent']==a].max()))
#     Min.append(int(df['spirit_servings'][df['continent']==a].min()))
# df1 = pd.DataFrame([lis,Mean,Min,Max]).T
# df1.rename(columns = {0:'continent',1:'mean',2:'min',3:'max'},inplace=True)
# print(df1)

print(df.groupby('continent').spirit_servings.agg(['mean','max','min']))

#########################################################################

################33333### todo:-  user.txt

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