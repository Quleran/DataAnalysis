import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

# Чтение данных из файла
df = pd.read_csv("27_B_17834.csv", encoding='utf-8', delimiter=';')

# Преобразование данных из строки в вещественные числа
df['X'] = df['X'].str.replace(',', '.').astype(float)
df['Y'] = df['Y'].str.replace(',', '.').astype(float)


'''
Используем метод Kmeans для для кластеризации на 3 кластера
------------------------------------------------------------------
Кластеризация (кластерный анализ) — метод анализа данных, при котором объекты группируются на подмножества (кластеры) по заданному критерию
K-means (k-средних) — это популярный итеративный алгоритм кластеризации данных, который разбивает набор точек на k кластеров. 
Каждый кластер характеризуется своим центром (средним значением), к которому ближе всего расположены точки данного кластера.
Алгоритм стремится минимизировать сумму квадратов расстояний от каждой точки до центра её кластера
'''
model = KMeans(n_clusters=3, random_state=0) # n_clusters = 3: кол-во кластеров
df['Cluster'] = model.fit_predict(df[['X', 'Y']]) # обучаем модель и присваиваем каждой точке номер кластера

real_centroids = []

for cluster in sorted(df['Cluster'].unique()):
    # Берём все точки кластера
    cluster_points = df[df['Cluster'] == cluster][['X', 'Y']].values

    # Считаем евклидовы расстояния между каждой парой точек внутри кластера и получаем матрицу расстояний
    distances = cdist(cluster_points, cluster_points, 'euclidean')

    # Суммируем расстояния от каждой точки до остальных
    sums = distances.sum(axis=1)

    # Точка с минимальной суммой расстояний — реальный центроид
    centroid = cluster_points[np.argmin(sums)]
    real_centroids.append(centroid)

# Преобразуем в массив numpy
real_centroids = np.array(real_centroids)

for i, c in enumerate(real_centroids):
    print(f"Кластер {i + 1}: центроид ({c[0]:.3f}, {c[1]:.3f})")

plt.figure(figsize=(6, 6))
plt.scatter(df['X'], df['Y'], c=df['Cluster'], alpha=0.3, marker='.')
plt.scatter(real_centroids[:, 0], real_centroids[:, 1], c='r', s=150, marker='.', label='Центроиды')
plt.title('Центроиды кластеров на данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
