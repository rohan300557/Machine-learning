import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


df = pd.read_csv('pima-indians-diabetes.csv')
df.columns  = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

# print(df.isnull().sum())

x = df.drop('label',axis=1)
y = df['label']
# print(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.30,random_state=5)    ### x is a input data and y is the crosspond output

tc = DecisionTreeClassifier()
tc.fit(x_train,y_train)

y_predict = tc.predict(x_test)

print(confusion_matrix(y_test, y_predict))