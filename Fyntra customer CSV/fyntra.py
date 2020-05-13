import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt

df = pd.read_csv('FyntraCustomerData.csv')
# print(df)

# 1..............
# sb.jointplot(x='Time_on_Website', y='Yearly_Amount_Spent',data=df,kind="reg")
# mlt.show()
# print('No there is not any correlation")

# 2..............
# sb.jointplot(x='Time_on_App', y='Yearly_Amount_Spent',data=df,kind="reg")
# mlt.show()
# print('Yes there is +ve correlation")

# 3..............
# sb.pairplot(df)
# mlt.show()

# 4..............
# sb.lmplot(x='Length_of_Membership',y='Yearly_Amount_Spent',data=df)
# mlt.show()
# print("Yes")

# 5..............
# x= df[['Time_on_App','Time_on_Website']]
# y=df['Yearly_Amount_Spent']
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=85)

# 6..............
# sb.scatterplot(x='Time_on_App',y='Time_on_Website',data=df)
# mlt.show()

# 7..............
# lm= LinearRegression()
# lm.fit(x_train,y_train)
# y_predict = lm.predict(x_test)
# y_score = lm.score(x_test,y_test)
# print(y_score)
# y_pre1 = sqrt(mean_squared_error(y_predict,y_test))
# print(y_pre1)

# 8..............
# sb.countplot(x='Time_on_Website',data=df)
# sb.countplot(x='Time_on_App',data=df)
# mlt.show()
# print("Company should focus on more App")









