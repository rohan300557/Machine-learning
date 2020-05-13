import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv('heart.csv')

# print(df)
# sb.catplot(x="age",hue="target",col='sex',kind="count",data = df)
# pd.crosstab(df.age,df.target).plot(kind='bar')    #### TODO: for getting count b/w age and targeted
##### 1=male ,, 0=female
# sb.boxplot(x='target',y='age',data=df)
# mlt.show()

cp1 = pd.get_dummies(df["cp"],drop_first=True)
ca1 = pd.get_dummies(df["ca"],drop_first=True)
thal1 = pd.get_dummies(df["thal"],drop_first=True)

df=pd.concat([df,ca1,cp1,thal1],axis=1)
df.drop(["ca","cp","thal"],axis=1,inplace=True)
# print(df)
# t1 = df[(df['sex']==1)&(df['target']==1)].count()
# print((t1['sex']/303)*100)
# t2 = df[(df['sex']==0)&(df['target']==1)].count()
# print((t2['sex']/303)*100)
# print(df.isnull().sum())

# print(df)

x = df.drop('target',axis=1)
y = df['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 5)
# print(x_test)
lm = LogisticRegression()
lm.fit(x_train,y_train)

y_predict = lm.predict(x_test)
# print(classification_report(y_test, y_predict))

# print(confusion_matrix(y_test, y_predict))


