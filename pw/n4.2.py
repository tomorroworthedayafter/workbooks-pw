import numpy as np
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.datasets import make_blobs #набор данных

#визуализация набора данных
centers = [[2,2],[4,5],[3,10]]#координаты центров
X, _ = make_blobs(n_samples = 500, centers = centers, cluster_std = 1)
plt.scatter(X[:,0],X[:,1])

#обучение с использованием входных данных
ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

#центры кластеров и ожидаемое количество кластеров согласно входным данным
print(cluster_centers)
n_clusters_ = len(np.unique(labels))
print("Estimated clusters:", n_clusters_)

#визуализация работы
colors = 10*['r.','g.','b.','c.','k.','y.','m.']
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

#центры
plt.scatter(cluster_centers[:,0],cluster_centers[:,1], marker = "x",color = 'k', s = 100, linewidths = 1, zorder = 10)
plt.show()
