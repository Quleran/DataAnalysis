import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

'''
1. Загрузите данные из файла "boston.csv" о недвижимости в различных
районах Бостона.
'''
df = pd.read_csv("boston.csv")
print(f'Датафрейм: \n{df}')
print('-' * 50)
'''
2. Проверьте, что у всех загруженных данных числовой тип.
'''
print(f'Типы данных: \n{df.dtypes}')
print('-' * 50)

'''
3. Проверьте, есть ли по каким-либо признакам отсутствующие данные.
Если отсутствующие данные есть – заполните их медианным
значением.
'''
missing = df.isnull()
print(f'Количество отсутствующих значений: \n{missing.sum()}')
print(f'\n Таблица: \n{missing}')
print('-' * 50)

'''
4. Посчитайте коэффициент корреляции для всех пар признаков.
Подсказка: воспользуйтесь методом corr() для датафрейма, чтобы
получить сразу всю корреляционную матрицу.
---------------------------
Корреляция - мера, которая отражает степень взаимосвязи между двумя переменными
'''
correlation_matrix = df.corr()
print(f'Матрица корреляции: \n{correlation_matrix}')
print('-' * 50)

'''
5. С помощью одной из библиотек визуализации постройте тепловую
карту (heatmap) по корреляционной матрице.
--------------------
Coolwarm - цветовая схема: синие оттенки для отрицательных значений,
           красные для положительных
'''
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', linewidths=0.5)
plt.title('Корреляционная матрица признаков')
plt.tight_layout()
plt.show()

'''
6. Выберите от 4 до 6 признаков, наиболее подходящих для анализа (на свое
усмотрение, выбор обоснуйте), которые в наибольшей степени
коррелируют с целевым признаком (ценой недвижимости).
'''
target_corr = correlation_matrix['MEDV'].sort_values(ascending=False)
print("Корреляция признаков с целевой переменной MEDV:")
print(target_corr)

selected_features = ["RM", "ZN", "LSTAT", "PTRATIO", "INDUS", "TAX"]
print(f"Выбранные признаки для анализа: {selected_features}")
print('-' * 50)

'''
7. Для каждого из выбранных признаков в паре с целевым признаком
постройте точечную диаграмму (диаграмму рассеяния).
'''
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.ravel()

for i, feature in enumerate(selected_features):
    axes[i].scatter(df[feature], df['MEDV'], alpha=0.6)
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('MEDV (цена)')
    axes[i].set_title(f'{feature} vs MEDV\nr = {target_corr[feature]:.3f}')

plt.tight_layout()
plt.show()

'''
8. Визуально убедитесь, что связь между выбранным признаком и целевым
прослеживается. Если на основе графика считаете, что зависимости
нет – исключите этот признак из дальнейшего рассмотрения (но при
этом как минимум 3 признака должно остаться в любом случае, если не
получается выбрать три признака, вернитесь к шагу 6).
'''
target_variable = 'MEDV'
factor_features = ['LSTAT', 'RM', 'PTRATIO']
print(f'Признаки для обучения: {factor_features}')
print('-' * 50)

x = df[factor_features].values.tolist()  # Признаки (факторы) для обучения
y = df[target_variable].tolist() # Целевая переменная


'''
10. Выполните разбиение датасета на обучающую и тестовую выборки в
соотношении 8:2. При формировании обучающей и тестовой выборок
строки из исходного датафрейма должны выбираться в случайном
порядке. Подсказка: можно воспользоваться функцией train_test_split из
библиотеки sklearn.model_selection.
'''
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=30)


'''
11. Из набора линейных моделей библиотеки sklearn возьмите
линейную регрессию, обучите ее на обучающем наборе.
'''
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)


'''
12. Получите векторы прогнозных значений целевой переменной на
обучающей и на тестовой выборках.
'''
y_train_pred = lin_reg.predict(X_train)
y_test_pred = lin_reg.predict(X_test)

'''
13.Посчитайте коэффициент детерминации
(R2)
и корень из
среднеквадратичной ошибки (RMSE) на обучающей и на тестовой
выборках. проанализируйте полученные данные. Если данные не
удовлетворительные, вернитесь к шагу 6
'''
r2_train = r2_score(y_train, y_train_pred)
rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
r2_test = r2_score(y_test, y_test_pred)
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))

print(f'Обучающая выборка: R2 = {r2_train:}, RMSE = {rmse_train:}')
print(f'Тестовая выборка: R2 = {r2_test:}, RMSE = {rmse_test:}')

'''
14. Постройте boxplot («ящик с усами») для целевого признака (MEDV).
Определите, какие значения можно считать выбросами. Указание.
Если по диаграмме выбросы определить не смогли, то для выполнения
дальнейших действий считайте выбросами значения MEDV=50.0.
'''
plt.figure(figsize=(8, 8))
sns.boxplot(y=df[target_variable])
plt.title('Boxplot для MEDV')
plt.show()

# Определение выбросов
outs = df[(df[target_variable] < 5.5) | (df[target_variable] > 36.5)]
print("Выбросы:\n", outs)

'''
15. Отфильтруйте исходные данные, удалив выбросы. Пересоздайте тестовую и обучающую выборки, переобучите модель.
Посчитайте показатели R2 и RMSE. Как они изменились? О чем это говорит?
Фильтруем данные
'''
data_filtered = df[(df[target_variable] > 5.5) & (df[target_variable] < 36.5)]

# Формируем список факторных признаков и целевую переменную
X_filtered = data_filtered[list(factor_features)]
y_filtered = data_filtered[target_variable]

# Разбиение датасета на обучающую и тестовую выборки
X_train_filt, X_test_filt, y_train_filt, y_test_filt = train_test_split(X_filtered, y_filtered, test_size=0.2, random_state=30)

# Линейная регрессия и обучение на новом наборе
lin_reg.fit(X_train_filt, y_train_filt)

# Векторы прогнозных значений целевой переменной на обучающей и на тестовой выборках (новых)
y_train_filt_pred = lin_reg.predict(X_train_filt)
y_test_filt_pred = lin_reg.predict(X_test_filt)

# Коэффициент детерминации (R2) и корень из среднеквадратичной ошибки (RMSE) на обучающей и на тестовой выборках.
# y_train_filt — это истинные значения целевой переменной для обучающего набора данных.
# y_train_filt_pred — это предсказанные значения, которые были получены моделью на том же наборе данных.
r2_train_filt = r2_score(y_train_filt, y_train_filt_pred)
rmse_train_filt = np.sqrt(mean_squared_error(y_train_filt, y_train_filt_pred))
r2_test_filt = r2_score(y_test_filt, y_test_filt_pred)
rmse_test_filt = np.sqrt(mean_squared_error(y_test_filt, y_test_filt_pred))

print("\nСравнение моделей до и после удаления выбросов")
print(f"R2 (тест до): {r2_test:.4f},  R2 (тест после): {r2_test_filt:.4f}")
print(f"RMSE (тест до): {rmse_test:.4f},  RMSE (тест после): {rmse_test_filt:.4f}")

'''
16. Из набора линейных моделей библиотеки sklearn возьмите гребневую регрессию (Ridge).
Обучите модель. Посчитайте показатели R2 и RMSE.
Обучаем модель с гребневой регрессией на обучающем наборе
'''
ridge_reg = Ridge()
ridge_reg.fit(X_train_filt, y_train_filt)


# Векторы прогнозных значений целевой переменной
y_train_ridge_pred = ridge_reg.predict(X_train_filt)
y_test_ridge_pred = ridge_reg.predict(X_test_filt)

# Линейная регрессия с регуляризацией для борьбы с переобучением
# Коэффициент детерминации (R2) и корень из среднеквадратичной ошибки (RMSE) на обучающей и на тестовой выборках.
# y_train_filt — это истинные значения целевой переменной для обучающего набора данных.
# y_train_ridge_pred — это предсказанные значения, которые были получены моделью на том же наборе данных.
r2_train_ridge = r2_score(y_train_filt, y_train_ridge_pred)
rmse_train_ridge = np.sqrt(mean_squared_error(y_train_filt, y_train_ridge_pred))
r2_test_ridge = r2_score(y_test_filt, y_test_ridge_pred)
rmse_test_ridge = np.sqrt(mean_squared_error(y_test_filt, y_test_ridge_pred))

print(f'\nГребневая регрессия - Обучающая выборка: R2 = {r2_train_ridge:}, RMSE = {rmse_train_ridge:}')
print(f'Гребневая регрессия - Тестовая выборка: R2 = {r2_test_ridge:}, RMSE = {rmse_test_ridge:}')

'''
17. Постройте полиномиальную регрессию с использованием полинома 3-й степени.
Посчитайте показатели R2 и RMSE. Сравните все полученные результаты.
Преобразование исходных признаков в полиномиальные
Полином 3-й степени degree=3
'''
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X_filtered)

X_train_poly, X_test_poly, y_train_poly, y_test_poly = train_test_split(X_poly, y_filtered, test_size=0.2, random_state=30)

# Обучение модели полиномиальной регрессии
lin_reg.fit(X_train_poly, y_train_poly)

# Векторы прогнозных значений целевой переменной
y_train_poly_pred = lin_reg.predict(X_train_poly)
y_test_poly_pred = lin_reg.predict(X_test_poly)

# Коэффициент детерминации (R2) и корень из среднеквадратичной ошибки (RMSE) на обучающей и на тестовой выборках.
# y_train_filt — это истинные значения целевой переменной для обучающего набора данных.
# y_train_poly_pred — это предсказанные значения, которые были получены моделью на том же наборе данных.
r2_train_poly = r2_score(y_train_poly, y_train_poly_pred)
rmse_train_poly = np.sqrt(mean_squared_error(y_train_poly, y_train_poly_pred))
r2_test_poly = r2_score(y_test_poly, y_test_poly_pred)
rmse_test_poly = np.sqrt(mean_squared_error(y_test_poly, y_test_poly_pred))

print(f'\nПолиномиальная регрессия - Обучающая выборка: R2 = {r2_train_poly:}, RMSE = {rmse_train_poly:}')
print(f'Полиномиальная регрессия - Тестовая выборка: R2 = {r2_test_poly:}, RMSE = {rmse_test_poly:}')

# Сравнение моделей

# Создаем таблицу сравнения моделей
print("\nСравнение моделей после удаления выбросов:\n")
print(f"{'Модель':<25}{'R2 train':<12}{'RMSE train':<12}{'R2 test':<12}{'RMSE test':<12}")
print("-" * 73)
print(f"{'Линейная регрессия':<25}{r2_train_filt:<12.4f}{rmse_train_filt:<12.4f}{r2_test_filt:<12.4f}{rmse_test_filt:<12.4f}")
print(f"{'Гребневая регрессия':<25}{r2_train_ridge:<12.4f}{rmse_train_ridge:<12.4f}{r2_test_ridge:<12.4f}{rmse_test_ridge:<12.4f}")
print(f"{'Полиномиальная регрессия':<25}{r2_train_poly:<12.4f}{rmse_train_poly:<12.4f}{r2_test_poly:<12.4f}{rmse_test_poly:<12.4f}")
