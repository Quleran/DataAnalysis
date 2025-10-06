import numpy as np
import pandas as pd

# Информация из файлов
countries = np.genfromtxt('global-electricity-generation.csv', dtype=str, delimiter=',',skip_header=1)[:, 0] # Страны
generat = np.genfromtxt('global-electricity-generation.csv', dtype=np.float64,delimiter=',', skip_header=1)[:, 1:] # Производство
consumpt = np.genfromtxt('global-electricity-consumption.csv', encoding='utf-8-sig', skip_header=1, delimiter = ',')[:, 1:] # Потребление

# Задание 2
average_generation = np.array([np.nanmean(row) if not np.all(np.isnan(row)) else np.nan
                                     for row in generat[:, -5:]])
average_consumption = np.array([np.nanmean(row) if not np.all(np.isnan(row)) else np.nan
                                      for row in consumpt[:, -5:]])


production_data = []
consumption_data = []

for i in range(len(countries)):
    if not np.isnan(average_generation[i]):
        production_data.append({
            'Страна': countries[i],
            'Производство': f"{average_generation[i]:.3f}"
        })
    if not np.isnan(average_consumption[i]):
        consumption_data.append({
            'Страна': countries[i],
            'Потребление': f"{average_consumption[i]:.3f}"
        })

print("\nСреднее производство электроэнергии за последние 5 лет:")
df_prod = pd.DataFrame(production_data)
df_prod.index = df_prod.index + 1  # Нумерация с 1
print(df_prod.to_string(index=True))

print("\nСреднее потребление электроэнергии за последние 5 лет:")
df_cons = pd.DataFrame(consumption_data)
df_cons.index = df_cons.index + 1
print(df_cons.to_string(index=True))

# 3.1 Суммарное потребление электроэнергии за каждый год
year_consumption = np.array(np.nansum(consumpt, axis=0))
print(f'\n3.1 Суммарное потребление электроэнергии за каждый год:\n{year_consumption}')

# 3.2 Максимальное количество электроэнергии, которое произвела одна страна за один год
year_max = np.nanmax(generat)
print(f'\n3.2 Максимальное количество электроэнергии:\n{year_max}')

# 3.3 Страны которые производят более 500 млрд. кВт*ч в год
more_500 = np.array(countries[average_generation > 500])
print(f'\n3.3 Производят более 500 млрд. кВт*ч в год:\n{more_500}')

# 3.4 10% стран, которые потребляют больше всего электроэнергии ежегодно в среднем за последние 5 лет
quant = np.nanquantile(average_consumption, 0.9)
consumption_max_country = np.array(countries[average_consumption >= quant])
print(f'\n3.4 10% стран, которые потребляют больше всегоэлектроэнергии ежегодно в среднем за последние 5 лет:\n{consumption_max_country}')

# 3.5 Список стран, которые увеличили производство электроэнергии в 2021 году по сравнению с 1992 годом более, чем в 10 раз
big_generation_country = np.array(countries[generat .T[-1] > generat .T[0] * 10])
print(f'\n3.5 Увеличили производство в 10 раз с 1992 года, посравнению с 2021:\n{big_generation_country}')

# 3.6 Список стран, которые в сумме за все годы потратили больше 100 млрд. кВт*ч электроэнергии и при этом произвели меньше, чем потратили
boring_country = np.array(countries[(np.nansum(consumpt, axis=1) > 100)
& (np.nansum(generat, axis=1) < (np.nansum(consumpt, axis=1)))])
print(f'\n3.6 Список стран, которые в сумме за все годы потратилибольше 100 млрд. кВт*ч электроэнергии и при этом произвели меньше, чем потратили:\n{boring_country}')

# 3.7. Какая страна потратила наибольшее количество электроэнергии в 2020 году
country = countries[np.nanargmax(consumpt[:, -2])]
print(f'\n3.7. Какая страна потратила наибольшее количество электроэнергии в 2020 году?:\n{country}')