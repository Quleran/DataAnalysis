import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

data = np.genfromtxt("data2.csv", dtype=float,
                        delimiter=';', encoding='utf-8-sig')
discounts = data[:, 0]  # Скидки
profits = data[:, 1]
x_val = [data[0, 0], data[(data.shape[0])//2, 0], data[-1, 0]]
y_val = [data[0, 1], data[(data.shape[0])//2, 1], data[-1, 1]]
matr = [[x**2, x, 1] for x in x_val]
coefs = solve(matr, y_val)
f_2 = coefs[0] * discounts**2 + coefs[1] * discounts + coefs[2]

vals = []
for r in data:
    vals.append(coefs[0]*r[0]**2 + coefs[1]*r[0] + coefs[2])
print("Скидка (%) | Прибыль (факт) | Прибыль (расчёт)")
print("-" * 45)
for i, (discount, profit) in enumerate(data):
    calculated = vals[i]
    print(f"{discount:10.1f} | {profit:14.2f} | {calculated:15.2f}")

RSS_2 = np.sum((profits - f_2) ** 2)
print("RSS для полинома 2-й степени:", RSS_2)



x_val_3 = [data[0, 0], data[(data.shape[0])//3, 0],
           data[(data.shape[0])//3*2, 0], data[-1, 0]]
y_val_3 = [data[0, 1], data[(data.shape[0])//3, 1],
           data[(data.shape[0])//3*2, 1], data[-1, 1]]
matr_3 = [[x**3, x**2, x, 1] for x in x_val_3]
coefs_3 = solve(matr_3, y_val_3)

vals_3 = []
for r in data:
    vals_3.append(coefs_3[0]*r[0]**3 + coefs_3[1]*r[0]
                  ** 2 + coefs_3[2]*r[0] + coefs_3[3])
print("\n\n\nСкидка (%) | Прибыль (факт) | Прибыль (расчёт)")
print("-" * 45)
for i, (discount, profit) in enumerate(data):
    calculated = vals_3[i]
    print(f"{discount:10.1f} | {profit:14.2f} | {calculated:15.2f}")
f_3 = coefs_3[0] * discounts**3 + coefs_3[1] * discounts**2 + coefs_3[2] * discounts + coefs_3[3]
RSS_3 = np.sum((profits - f_3) ** 2)
print("RSS для полинома 3-й степени:", RSS_3)


print("\nЗначение прибыли при значениях скидки в 6 и 8 процентов:\n",
      coefs_3[0]*6.0**3 + coefs_3[1]*6.0**2 + coefs_3[2]*6.0 + coefs_3[3], coefs_3[0]*8.0**3 + coefs_3[1]*8.0**2 + coefs_3[2]*8.0 + coefs_3[3])

plt.figure(figsize=(10, 6))
plt.plot(discounts, profits, '-', label='Данные из файла')
plt.plot(discounts, f_2, '-', label='Полином 2-й степени')
plt.xlabel('Скидка')
plt.ylabel('Прибыль')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(discounts, profits, '-', label='Данные из файла')
plt.plot(discounts, f_3, '-', label='Полином 3-й степени')
plt.xlabel('Скидка')
plt.ylabel('Прибыль')
plt.legend()
plt.show()


