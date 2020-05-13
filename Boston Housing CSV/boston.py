import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


df  = pd.read_csv("BostonHousing.csv")
# # print(df.isnull().sum())
t1 = df.corr()
t2 = sb.heatmap(t1,annot=True)
x = df[['rm','lstat','ptratio']]
y = df['medv']
print(y)

# ax = sb.pairplot(df[['rm','lstat','ptratio']])

# ax = sb.distplot(x)

# sb.lmplot(x = 'medv',y='rm',data=df)
# sb.lmplot(x = 'medv',y='lstat',data=df)
# sb.lmplot(x = 'medv',y='ptratio',data=df)

####For training and testing the data...........
x = df[['rm','lstat','ptratio']]   #### Train
y = df['medv']   #### output that
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=10)    ### x is a input data and y is the crosspond output
# print(x_train)   #### random state just fix the random data state which will not change the


lm = LinearRegression()

lm.fit(x_train,y_train)
# print(lm.intercept_)     ### To get the intercept

y_predict = lm.predict(x_test)
# print(y_predict)

# mlt.scatter(y_predict,y_test)
# mlt.show()


# y_score = lm.score(x_test,y_test)
# print(y_score)

y_pre = mean_absolute_error(y_test,y_predict)
y_pre1 = mean_squared_error(y_predict,y_test)
y_pre2 = r2_score(y_predict,y_test)
# print(y_pre)
# print(y_pre1)
# print(y_pre2)