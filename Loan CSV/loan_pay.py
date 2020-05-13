import pandas as pd
import seaborn as sb
import matplotlib.pyplot as mlt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


df = pd.read_csv('train_new.csv')
# print(df.isnull().sum())

df.drop(["Married","Property_Area","Education","Loan_ID","Dependents"],inplace=True,axis=1)

df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean(),inplace=True)
df.dropna(inplace=True)

# print(df.isnull().sum())


status = pd.get_dummies(df["Loan_Status"],drop_first=True)
employed = pd.get_dummies(df["Self_Employed"],drop_first=True)
gender = pd.get_dummies(df["Gender"],drop_first=True)
# print(employed)

df = pd.concat([df,status,gender,employed],axis=1)
df.drop(["Loan_Status","Self_Employed","Gender"],axis=1,inplace=True)
# print(df)

x = df.drop("Y",axis=1)
y = df["Y"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 101)

lm = LogisticRegression()
lm.fit(x_train,y_train)

y_predict = lm.predict(x_test)
print(classification_report(y_test, y_predict))

print(confusion_matrix(y_test, y_predict))