import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


df = pd.read_csv('kyphosis.csv')
# sb.pairplot(df)
# sb.pairplot(df,hue='kyphosis')

# mlt.show()
x = df[['Age','Number','Start']]
y = df['Kyphosis']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.28,random_state=1)

rfc = RandomForestClassifier()
rfc.fit(x_train,y_train)

y_predict = rfc.predict(x_test)
# print(y_predict)

print(confusion_matrix(y_test, y_predict))

print(df['Kyphosis'].value_counts()) ###3  give the no.count of pre and abs