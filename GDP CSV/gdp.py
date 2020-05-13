import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


df1  = pd.read_csv("gdp_per_capita.csv",encoding='cp1252')
df2 = pd.read_csv("oecd_bli_2015.csv",encoding='cp1252')
df3 = pd.merge(df1,df2)
df3.drop(["Reference Period Code","Reference Period"],axis=1,inplace=True)
# print(df3.head())
# print(df3.tail())

# print(df3.isnull().sum())
# print(df3.info())

# print(df3.columns)
t1 = df3.corr()
# print(t1)
#
# t2 = sb.heatmap(t1,annot=True  )
# # x = df3[['Value','PowerCode Code','Estimates Start After']]
# # y = df3[['Estimates Start After']]
#
#
# # x = df3[['Value']]
# # y = df3[['Estimates Start After']]
#
#
# # t1 = sb.pairplot(df3)
# # mlt.show()
#
#
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=20)    ### x is a input data and y is the crosspond output
# # print(x_train)
# lm = LinearRegression()
# lm.fit(x_train,y_train)
#
# y_predict = lm.predict(x_test)
#
# y_score = lm.score(x_test,y_test)    ### range of output -1 to 1
# # print(y_score)
#
#
# y_pre = mean_absolute_error(y_test,y_predict)
# y_pre1 = mean_squared_error(y_predict,y_test)
# y_pre2 = r2_score(y_predict,y_test)
# # print(y_pre)
# # print(y_pre1)
# # print(y_pre2)

# print(df3.isnull().values.any())
# print(df3.isnull())
sb.heatmap(df3.isnull())   #### For False its blue(0.0) and For True its (1.0)
mlt.show()

## Get the log of data and apply theorm for improve data