import seaborn as sb
import random
import pandas as pd
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import r2_score

a1=[]
a2=[]
a3=[]
d = {'x':a1,'y':a2,'z':a3}
for a in range(1,101):
    n = random.randint(1,100)
    a1.append(n)
for a in range(1,101):
    n = random.randint(1,100)
    a2.append(n)
for i in range(len(a1)):
    # z = a1[i] + a2[i]
    z = a1[i]+a2[i]
    a3.append(z)
df = pd.DataFrame(d,columns=['x','y','z'])
df.to_csv("addition.csv")

x=df.drop('z',axis=1)
y=df['z']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=10)    ### x is a input data and y is the crosspond output

lm = LinearRegression()

lm.fit(x_train,y_train)
y_predict = lm.predict(x_test)
print(y_predict)

