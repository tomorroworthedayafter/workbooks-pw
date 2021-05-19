#Построение графиков

import numpy as np
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20] # Список № 1
y = [1, 7, 3, 5, 11]   # Список № 2

plt.plot(x, y, label='steel price')            
plt.title('Chart price', fontsize=15)
plt.xlabel('Day', fontsize=12, color='blue')   # Цвет
plt.ylabel('Price', fontsize=12, color='blue') # Цвет
plt.legend()
plt.grid(True)
plt.text(15, 4, 'grow up!')

plt.show()
