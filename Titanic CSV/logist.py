import pandas as pd
import matplotlib.pyplot as mlt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# print(train_df.isnull().sum())
p1 = (train_df['Age'].isnull().sum()/891)*100     ### TODO: for getting percentage
p2 = (train_df['Cabin'].isnull().sum()/891)*100
p3 = (train_df['Embarked'].isnull().sum()/891)*100

# print('Null data for Age:',p1,'%')    ### TODO: for getting percentage
# print('Null data for Cabin:',p2,'%')
# print('Null data for Embarked',p3,'%')

# sb.countplot(x='Survived',hue='Pclass',data=train_df)    ###TODO: who survived in the pclass
# sb.countplot(x='Survived',hue='Sex',data=train_df)     ###TODO: who survived in the Gender basis
# sb.countplot(x='Age',hue='Pclass',data=train_df)    ###TODO: who survived in the pclass

# sb.distplot(train_df['Age'].dropna(), kde=False, bins=30, color='Green')   ###TODO:Kernal density estimation

# sb.boxplot(x='Pclass',y='Age',data=train_df)    ####TODO: getting mean age in the pclass
# mlt.show()

def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(train_df[train_df["Pclass"] == Pclass]["Age"].mean())
    else:
        return Age

train_df["Age"] = train_df[["Age", "Pclass"]].apply(add_age,axis=1)
# print(train_df.iloc[5])
########### NOw this is to do with Fillna function#######################################3
#TODO: Not Use THis code in # Its total mean of age with considering Pclass
# train_df['Age'].fillna(train_df['Age'].mean(),inplace=True)

# train_df["Age"].fillna(train_df["Age"].mean(skipna=True), inplace=True)
# print(train_df.isnull().sum())
# print(train_df['Age'])
# print(train_df.iloc[17])
# x= train_df.copy()
# train_df['Age'].fillna(train_df['Age'].mean(),inplace=True)
# # print(train_df)
# print(train_df.iloc[17])
#######################################################################################

pclass = pd.get_dummies(train_df["Pclass"],drop_first=True)   ###Todo: Make the dummies of the values corresponds to its class
sex = pd.get_dummies(train_df["Sex"],drop_first=True)   ### Todo: Drop_first will drop the first column in the output
embarked = pd.get_dummies(train_df["Embarked"],drop_first=True)

# print(pclass)
# print(sex)
# print(embarked)
train_df = pd.concat([train_df,sex,pclass,embarked],axis=1)
train_df.drop(["PassengerId","Pclass","Name",'Cabin',"Sex","Ticket","Embarked"],axis=1,inplace=True)
# print(train_df)
x=train_df[['Age', 'SibSp', 'Parch', 'Fare', 'male', 2, 3, 'Q','S']]
y=train_df['Survived']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=10)

lm = LogisticRegression()
lm.fit(x_train,y_train)

y_predict = lm.predict(x_test)
# print(y_predict)

# print(classification_report(y_test,y_predict))
print(confusion_matrix(y_test, y_predict))     ####  MAtrixx of TT TF FT Ff

#TODO:Graph 