#Работа с линейным графиком

import numpy as np
import matplotlib.pyplot as plt

plt.subplot(3, 1, 1)
x1 = [1, 5, 10, 15, 20] # Список №1
y1 = [1, 7, 3, 5, 11]   # Список №2


#Вывод графика

y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.plot(x1, y1, '-', x1, y2, '--', x1, y3, '-.', x1, y4, ':')


plt.subplot(3, 1, 2)
x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, 'ro')

plt.subplot(3, 1, 3)
plt.plot(x, y, 'bx')
plt.show()
