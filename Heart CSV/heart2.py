import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

df = pd.read_csv('heart.csv')
# print(df)

# sb.pairplot(df,hue='species')
# mlt.show()


cp1 = pd.get_dummies(df["cp"],prefix='cp',drop_first=True)
ca1 = pd.get_dummies(df["ca"],prefix='ca',drop_first=True)
thal1 = pd.get_dummies(df["thal"],prefix='thal',drop_first=True)

df=pd.concat([df,ca1,cp1,thal1],axis=1)
df.drop(["ca","cp","thal"],axis=1,inplace=True)


x = df.drop('target',axis=1)
y = df['target']

# print(x.columns)

ss = StandardScaler()
x = ss.fit_transform(x)
# print(ss.transform(x,copy=True))
df = pd.DataFrame(x,columns=['age', 'sex', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang',
       'oldpeak', 'slope', 'ca_1', 'ca_2', 'ca_3', 'ca_4', 'cp_1', 'cp_2',
       'cp_3', 'thal_1', 'thal_2', 'thal_3'])

x=df
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.30,random_state=5)    ### x is a input data and y is the crosspond output

kn = KNeighborsClassifier(n_neighbors=3)    ### any odd number 1,3,5
kn.fit(x,y)

y_predict = kn.predict(x_test)

print(accuracy_score(y_test,y_predict))
print(confusion_matrix(y_test, y_predict))
