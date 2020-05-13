import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('data.csv')
df.drop('Unnamed: 32',axis=1,inplace=True)

# print(df.isnull().sum())

# t = df.corr()
# sb.heatmap(t,annot=True)
# sb.countplot(df['diagnosis'])
# mlt.show()

diag = pd.get_dummies(df['diagnosis'],prefix='diagnosis',drop_first=1)
df.drop(['id','diagnosis'],axis=1,inplace=True)
df = pd.concat([df,diag],axis=1)
# print(df.columns)

##########TODO: column removed becoz many of them related to each other....
df.drop(['perimeter_mean', 'area_mean', 'concavity_mean','concave points_mean',
       'perimeter_se','area_se','concavity_se','concave points_se','radius_worst',
       'texture_worst','perimeter_worst','area_worst', 'smoothness_worst','compactness_worst',
       'concavity_worst', 'concave points_worst','symmetry_worst',
       'fractal_dimension_worst'],axis=1,inplace=True)

# print(df.isnull().sum())

# t = df.corr()
# sb.heatmap(t,annot=True)
# mlt.show()

x=df.drop('diagnosis_M',axis=1)
y=df['diagnosis_M']

########################################################################################
# x_train,x_test,y_train,y_test =  train_test_split(x,y,test_size=.25,random_state=10)
# # print(x_test)
#
# lr=LogisticRegression()
# lr.fit(x_train,y_train)
#
# y_predict = lr.predict(x_test)
# print(confusion_matrix(y_test,y_predict))
# print(accuracy_score(y_test,y_predict))
# print('Accuracy : 88 %')
###########################################################################################
# le = LabelEncoder()
# y = le.fit_transform(y)
# x_train,x_test,y_train,y_test =  train_test_split(x,y,test_size=.25,random_state=10)

# kn = KNeighborsClassifier(n_neighbors=1)
# kn.fit(x_train,y_train)
#
# y_predict = kn.predict(x_test)
#
# print(confusion_matrix(y_test,y_predict))
# print(accuracy_score(y_test,y_predict))
# print('Accuracy : 81 %')
#############################################################################################