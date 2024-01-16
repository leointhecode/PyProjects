from sklearn.datasets import make_moons
from matplotlib import pyplot as plt

x, y = make_moons(noise=0.1, random_state=453)
c1, c2 = x[y == 0], x[y == 1]

plt.scatter(c1[:, 0], c1[:, 1], c='red')
plt.scatter(c2[:, 0], c2[:, 1]-0.9, c='blue')
