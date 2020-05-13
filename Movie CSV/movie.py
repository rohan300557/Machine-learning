import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


df = pd.read_csv("file.tsv",sep='\t')
df1 = pd.read_csv("Movie_Id_Titles.csv")
# p1 = pd.DataFrame(df,columns=['User_id','Item_id','Rating','Timestamp'])
df.columns = ['user_id','item_id','rating','timestamp']
df2 = df.merge(df1,on='item_id')
# print(df2)
t1 = df2.corr()
sb.heatmap(t1,annot=True)
# mlt.show()

y = df[['item_id']]
x = df[['user_id','rating','timestamp']]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=10)    ### x is a input data and y is the crosspond output

lm = LinearRegression()
lm.fit(x_train,y_train)
y_predict = lm.predict(x_test)
y_score = lm.score(x_test,y_test)
print(y_score)
y_pre = mean_absolute_error(y_test,y_predict)
y_pre1 = mean_squared_error(y_predict,y_test)
y_pre2 = r2_score(y_predict,y_test)
# print(y_pre)
# print(y_pre1)
# print(y_pre2)
