from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.linalg import svd
r1=[[1,2,3],[32,34,34]]

iris = datasets.load_iris()
data=iris['data']
u,sigma,Vt=svd(data)
print("U",u)
print("sigma\n",sigma)
print("Vt\n",Vt)

