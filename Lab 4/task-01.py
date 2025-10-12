import numpy as np
import pandas as pd
from numpy.ma.extras import average

"""
1. Сгенерировать случайным образом массив numpy из 1000 значений
нормально распределенной случайной величины (numpy.random.normal) 
с мат. ожиданием M = 1.0 и стандартным отклонением s = 1.0.
Преобразовать его в объект Series.
"""
M = 1.0
s = 1.0
normal_array = np.random.normal(M, s, 1000)
series_array = pd.Series(normal_array)
print(f'1. Сгенерированный массив из 1000 значений: \n{series_array} ')


"""
2. Вычислить, какая доля всех значений находится в диапазоне (M-s; M+s).
3. Вычислить, какая доля всех значений находится в диапазоне (M-3s; M+3s).
"""
range_1 = ((series_array > (M - s)) & (series_array < (M + s))).sum()
fraction_1 = range_1 / len(series_array)
print(f'\n2. Доля всех значений в диапазоне (M-s; M+s): {fraction_1}')

range_2 = ((series_array > (M - 3 * s)) & (series_array < (M + 3 * s))).sum()
fraction_2 = range_2 / len(series_array)
print(f'\n3. Доля всех значений в диапазоне (M-3s; M+3s): {fraction_2}')


"""
4. Заменить каждое значение x в серии на его квадратный корень
(numpy.sqrt(x)). Результат записать в новый объект Series. Почему
возникает предупреждение, и что происходит с теми значениями, для
которых возникает предупреждение?
"""
normal_array_sqrt = np.sqrt(normal_array)
series_array_sqrt = pd.Series(normal_array_sqrt)
print(f'\n4. Серия с заменой значений на квадратный корень:\n{series_array_sqrt}')


"""
5. Посчитать среднее арифметическое для получившихся значений.
Отсутствующие значения (NaN) учитываться не должны.
"""
average_array = series_array_sqrt.mean()
print(f'\n5. Среднее арифметическое для получившихся значений: {average_array}')


"""
6. На основе двух объектов Series (исходного и полученного на шаге 4)
создать DataFrame с двумя столбцами. Названия (явные индексы) для
столбцов: «number» и «root» соответственно. Явные индексы для строк не
задавать. Вывести первые 6 строк из созданного датафрейма.
"""
df = pd.DataFrame({
    'number': series_array,
    'root': series_array_sqrt
})
print(f'\n6. DataFrame:\n{df.head(6)}')


"""
7. С помощью функции query найти в датафрейме записи, в которых
значение квадратного корня находится в диапазоне от 1.8 до 1.9. Вывести
результат.
"""
result = df.query('root >= 1.8 and root <= 1.9')
print(f'\n 7. Записи, где квадратный корень в диапазоне от 1.8 до 1.9:\nКол-во записей: {len(result)}\n{result}')
