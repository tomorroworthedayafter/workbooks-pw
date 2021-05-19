#Построение диаграммы для категориальных данных

import matplotlib.pyplot as plt
import numpy as np

fruits = ["apple", "peach", "orange", "bannana", "melon"]
counts = [34, 25, 43, 31, 17]

plt.bar(fruits, counts)
plt.title("Fruits!")
plt.xlabel("Fruit")  # Ось X
plt.ylabel("Count" ) # Ось Y

plt.show()
