import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

#входные данные
A = np.array([[3.1, 2.3], [2.3, 4.2], [3.9, 3.5], [3.7, 6.4], [4.8, 1.9],
             [8.3, 3.1], [5.2, 7.5], [4.8, 4.7], [3.5, 5.1], [4.4, 2.9]])

#определение ближайших соседей
k = 3

#тестовые данные
test_data = [3.3, 2.9]

#визуализация входных данных
plt.figure()
plt.title("input data")
plt.scatter(A[:, 0], A[:, 1], marker = "o", s = 100, c = "black")

#построим ближайшего соседа, обучим его
knn_model = NearestNeighbors(n_neighbors = k, algorithm = "auto").fit(A)
distances, indices = knn_model.kneighbors([test_data])

#координаты K ближайших соседей
print("\nk ближайших соседей: ")
for rank, index in enumerate(indices[0][:k], start = 1):
    print(str(rank) + " is", A[index])

#визуализация
plt.title("K Nearest Neighbors")
plt.scatter(A[:, 0], A[:, 1], marker="o", s=100, c="k")
plt.scatter(A[indices][0][:][:, 0], A[indices][0][:][:, 1], marker = "o", s=250, facecolors = 'none', edgecolors='purple')
plt.scatter(test_data[0], test_data[1], marker = "x", c = "purple", s = 100)

plt.show()
