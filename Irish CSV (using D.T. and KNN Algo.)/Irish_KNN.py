from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.5,random_state=10)

# from sklearn.neighbors import KNeighborsClassifier
# dc = KNeighborsClassifier()

dc = tree.DecisionTreeClassifier()
dc.fit(x_train,y_train)
predict = dc.predict(x_test)
print(accuracy_score(y_test,predict))