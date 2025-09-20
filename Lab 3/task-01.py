import numpy as np

# Информация из файлов
countries = np.genfromtxt('global-electricity-generation.csv', dtype=str, delimiter = ',')[1:, 0] # Страны
generat = np.genfromtxt('global-electricity-generation.csv', delimiter = ',')[1:, 1:] # Производство
consumpt = np.genfromtxt('global-electricity-consumption.csv', delimiter = ',')[1:, 1:] # Потребление

# Суммарное (по всем странам) потребление электроэнергии за каждый год
a1 = consumpt.sum(axis=0)
print(a1)