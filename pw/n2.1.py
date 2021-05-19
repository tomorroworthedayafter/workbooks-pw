#Предварительная обработка данных

import numpy as np
from sklearn import preprocessing

input_data = np.array([[2.1, -1.9, 5.5],
                      [-1.5, 2.4, 3.5],
                      [0.5, -7.9, 5.6],
                      [5.9, 2.3, -5.8]])

# Применение методов предварительной обработки

# Бинаризация
data_binarized = preprocessing.Binarizer(threshold = 0.5).transform(input_data)
print("\tБинаризация\n", data_binarized)

# Среднее удаление
print("\n\tСреднее удаление\nmean = ", input_data.mean(axis = 0)) # Средние значение
print("Standart deviation = ", input_data.std(axis = 0)) # Среднее отклонение

data_scaled = preprocessing.scale(input_data)
print("standart deviation = ", data_scaled.std(axis = 0))

# Пересчет
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data) # Вычисление -> преобразование
print ("\n\tПересчет\n", data_scaled_minmax)

#Нормализация
data_normalized_l1 = preprocessing.normalize(input_data, norm = 'l1')
print("\n\tL1 нормализация\n", data_normalized_l1)

data_normalized_l2 = preprocessing.normalize(input_data, norm = 'l2') 
print("\n\tL2 нормализация\n", data_normalized_l2)
