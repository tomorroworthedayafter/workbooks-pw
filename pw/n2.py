# Несколько графиков на одном поле

import matplotlib.pyplot as plt
import numpy as np

# Линейная зависимость
x = np.linspace(0, 10, 50)
y1 = x

# Квадратичная зависимость
y2 = [i**2 for i in x]
# Построение графика
plt.title("Зависимости: y1 = x, y2 = x^2")
plt.xlabel("x")                             # Ось x
plt.ylabel("y1, y2")                        # Ось y
plt.grid()                                  # Отображение сетки
plt.plot(x, y1, x, y2)                      # График

plt.show()
