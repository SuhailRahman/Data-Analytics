from sklearn import datasets
from sklearn.decomposition import PCA


# import some data to play with
iris = datasets.load_iris()

data=iris['data']
c = PCA(n_components=2).fit_transform(data)
print(c)