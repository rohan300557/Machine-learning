import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

## 1 A.)............................................................
df  = pd.read_csv("prisoners.csv")
# print(df)
## 1 B.)............................................................
# print(df.describe())
# print(df.columns)
# print(df.isnull().sum())
# print(df)

## 2 A.)............................................................
# t1 = df[['No. of Inmates benefitted by Elementary Education','No. of Inmates benefitted by Adult Education'
#           ,'No. of Inmates benefitted by Higher Education','No. of Inmates benefitted by Computer Course']]
# df["total_benefited"]=t1.sum(axis=1)
# print(df)

## 2 B.)............................................................
# t1 = df[['No. of Inmates benefitted by Elementary Education','No. of Inmates benefitted by Adult Education'
#            ,'No. of Inmates benefitted by Higher Education','No. of Inmates benefitted by Computer Course']]
# df["total_benefited"]=t1.sum(axis=1)
# df.loc[35,'total_benefited']= str(df['total_benefited'].sum())
# df.loc[35,'STATE/UT']='TOTALS'
# df.loc[35,'YEAR']='2013'
# for t2 in t1:
#     df.loc[35,t2] = str(df[t2].sum())   #### JUST THE VALUES are coming in ##### FLOAT ######
# print(df)

## 3 A.)............................................................
# t1 = df[['No. of Inmates benefitted by Elementary Education','No. of Inmates benefitted by Adult Education'
#           ,'No. of Inmates benefitted by Higher Education','No. of Inmates benefitted by Computer Course']]
# df["total_benefited"]=t1.sum(axis=1)
# t2 = plt.bar(df['STATE/UT'],df['total_benefited'])
# plt.xlabel("STATE/UT")
# plt.ylabel("total_benefitted")
# plt.show()

## 3 B.)............................................................
t1 = df[['No. of Inmates benefitted by Elementary Education','No. of Inmates benefitted by Adult Education'
          ,'No. of Inmates benefitted by Higher Education','No. of Inmates benefitted by Computer Course']]
df["total_benefited"]=t1.sum(axis=1)
t1 = df["STATE/UT"]
t2 = df["total_benefited"]
plt.pie(t2, labels = t1,autopct='')
plt.show()