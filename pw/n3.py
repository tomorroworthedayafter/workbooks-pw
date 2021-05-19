# Разделенные поля с графиками

import matplotlib.pyplot as plt
import numpy as np

# Линейная зависимость
x = np.linspace(0, 10, 50)
y1 = x

# Квадратичная зависимость
y2 = [i**2 for i in x]

plt.figure(figsize=(9, 9)) # Размер общего поля
plt.subplot(2, 1, 1)  # Расположение поля в области графика
plt.plot(x, y1)
plt.title("Зависимости: y1 = x, y2 = x^2")
plt.ylabel("y1", fontsize=14) # Ось y
plt.grid(True) # Отображение сетки
plt.subplot(2, 1, 2)
plt.plot(x, y2) # Построение графика
plt.xlabel("x", fontsize=14) # Ось x
plt.ylabel("y2", fontsize=14) # Ось y
plt.grid(True) # Отображение сетки

plt.show()
