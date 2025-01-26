import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

X, y = make_circles(n_samples=100, factor=0.8, noise=0.1)
plt.scatter(X[:,0],X[:,1], c=y)
plt.show()
