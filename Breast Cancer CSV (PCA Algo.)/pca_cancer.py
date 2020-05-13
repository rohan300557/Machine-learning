import scipy.linalg as la
import pandas as pd
import seaborn as sb
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = datasets.load_breast_cancer()
x = df.data
y = df.target

features = df.feature_names
df = pd.DataFrame(data=x, columns=features)
# print(df)

ss = StandardScaler()
X = ss.fit_transform(x)
pca = PCA(n_components=3)
p = pca.fit_transform(X)
# print(p.shape)


cm = np.cov(X, rowvar=False, bias=True) #### covariance matrix
# print(cm)


eigvals, eigvecs = la.eig(cm)
# print(eigvals)
# print(eigvecs)



# fig = plt.figure(figsize=(15, 8))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(p[:,0], p[:,1], p[:,2], c=y, s=60)
# ax.set_xlabel("PC1")
# ax.set_ylabel("PC2")
# ax.set_zlabel("PC3")
# ax.set_title("PCA on the Breast cancer dataset")
# ax.view_init(20, 45)
# plt.show()

