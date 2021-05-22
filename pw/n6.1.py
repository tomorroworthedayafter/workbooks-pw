import matplotlib.pyplot as plt
import neurolab as nl
import numpy as np

#Целвые значения
input = [[0, 0], [0, 1], [1, 0], [1, 1]]
target = [[0], [0], [0], [1]]

net = nl.net.newp([[0, 1],[0, 1]], 1)
error_progress = net.train(input, target, epochs=100, show=10, lr=0.1) #Тренировка сети

#Визуализация и построение графика
plt.figure()
plt.plot(error_progress)
plt.xlabel('Number of epochs')
plt.ylabel('Training error')
plt.grid()
plt.show()
