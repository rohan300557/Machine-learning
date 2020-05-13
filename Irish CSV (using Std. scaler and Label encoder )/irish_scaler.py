import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

df = pd.read_csv('IRIS.csv')
# print(df)

# sb.pairplot(df,hue='species')
# mlt.show()

x=df.drop('species',axis=1)
y= df['species']
# print(x)

# print(x_test)

# le=LabelEncoder()
# y = le.fit_transform(y)
# print(y)

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.30,random_state=5)    ### x is a input data and y is the crosspond output


# a1=[]
# a2=[]
# for a in range(1,30):
#     if a%2!=0:
#         a2.append(a)
#         kn = KNeighborsClassifier(n_neighbors=a)  ### any odd number 1,3,5
#         kn.fit(x, y)
#         y_predict = kn.predict(x_test)
#         # print(y_predict)
#         p = accuracy_score(y_test,y_predict)
#         a1.append(p)
        ######## print(confusion_matrix(y_test, y_predict))    ##### f_neig

# mlt.plot(a2,a1)
# mlt.show()
#####################################################################
ss = StandardScaler()
x = ss.fit_transform(x)
# print(ss.transform(x,copy=True))
df = pd.DataFrame(x,columns=['sepal_length','sepal_width','petal_length','petal_width'])
# pd.DataFrame(x,columns=x.columns)   ##TODO : Or we can do like this
x=df
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.30,random_state=5)    ### x is a input data and y is the crosspond output

kn = KNeighborsClassifier(n_neighbors=3)    ### any odd number 1,3,5
kn.fit(x,y)

y_predict = kn.predict(x_test)
# print(y_predict)
print(accuracy_score(y_test,y_predict))
print(confusion_matrix(y_test, y_predict))    ##### f_neig



#### MAKE A 100 rows of data set with x,y,z  and in this x+y=z ,Use leaner regress