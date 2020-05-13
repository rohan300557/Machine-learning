from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()
test_idx = [0,50,100]
x_target = np.delete(iris.target,test_idx)
x_data = np.delete(iris.data,test_idx,axis= 0)
# print(iris.target)
y_target = iris.target[test_idx]
y_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(x_data,x_target)
# print(y_target)
# print(clf.predict(y_data ))

# from sklearn.externals.six import StringIO
# import pydotplus
# dot_data = StringIO()
# tree.export_graphviz(clf,
#                      out_file=dot_data,
#                      feature_names=iris.feature_names,
#                      class_names=iris.target_names,
#                      filled=True, rounded=True,
#                      impurity=False)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf("iris.pdf")
