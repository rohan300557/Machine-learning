import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
df = pd.read_csv('voice.csv')

# print(df)
# print(df.isnull().sum())

# sb.boxplot(x='label',y='meanfreq',data=df)
# mlt.show()



#############todo: Q 1.
# x=df.drop('label',axis=1)
# y=df['label']
#
# le = LabelEncoder()
# y= le.fit_transform(y)
#
# oe = OneHotEncoder()
# y=oe.fit_transform(x,y)
#
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.30,random_state=5)
#
# print(x_test)

#############todo: Q 2.
# label = pd.get_dummies(df["label"],drop_first=True)
# df = pd.concat([df,label],axis=1)
# df.drop('label',axis=1,inplace=True)
# x = df.drop('male',axis=1)
# y= df['male']
# # print(x)
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=10)
#
# lm = LogisticRegression()
# lm.fit(x_train,y_train)
# y_predict = lm.predict(x_test)
# print(classification_report(y_test,y_predict))
# print(accuracy_score(y_test,y_predict))
# # print('The accuracy on the test set  : 93%')

#############todo: Q 3.
# df.drop(['centroid','maxdom','dfrange','kurt'],axis=1,inplace=True)
# a = df.corr()
# print(a)
# t = sb.heatmap(a,annot=True)
# mlt.show()

#############todo: Q 4.
# df.drop(['centroid','maxdom','dfrange','kurt'],axis=1,inplace=True)
# label = pd.get_dummies(df["label"],drop_first=True)
# df = pd.concat([df,label],axis=1)
# df.drop('label',axis=1,inplace=True)
# x = df.drop('male',axis=1)
# y= df['male']
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=10)
#
# lm = LogisticRegression()
# lm.fit(x_train,y_train)
# y_predict = lm.predict(x_test)
# print(classification_report(y_test,y_predict))
# print(accuracy_score(y_test,y_predict))
# # print('The accuracy on the test set  : 93%')
