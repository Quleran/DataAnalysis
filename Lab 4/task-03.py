import pandas as pd

df = pd.read_csv('datasets/telecom_churn.csv')

"""
1. Выведите общую информацию о датафрейме с помощью методов info или
describe. Есть ли отсутствующие данные?
"""
print(f'2. Информация по признакам:')
df.info()


"""
2. С помощью метода value_counts определите, сколько клиентов активны, а
сколько потеряно. Сколько процентов клиентов в имеющихся данных
активны, а сколько потеряны?
"""
total_count = len(df)
true_count = df['Churn'].sum()
false_count = total_count - true_count
print(f'\n2. Количество активных клиентов: {false_count}\n   Количество потерянных клиентов {true_count}')
print(f'   Процентов клиентов в имеющихся данных активны:  {(false_count/total_count) * 100}\n   Процентов клиентов в имеющихся данных потеряны: {(true_count/total_count)*100}')


"""
3. Добавьте дополнительный столбец в датафрейм - средняя
продолжительность одного звонка (вычислить как суммарная
продолжительность всех звонков, деленная на суммарное количество
всех звонков). Отсортируйте данные по этому значению по убыванию и
выведите 10 первых записей.
"""
total_minutes = df['Total day minutes'] + df['Total eve minutes'] + df['Total night minutes']
total_calls = df['Total day calls'] + df['Total eve calls'] + df['Total night calls']

df['Call_duration'] = total_minutes / total_calls
df_sorted = df.sort_values('Call_duration', ascending=False)
print(f'\n3. Самая большая продолжительность звонка:\n{df_sorted.head(10)}')


"""
4. Сгруппируйте данные по значению поля «Churn» и вычислите среднюю
продолжительность одного звонка в каждой категории. Есть ли
существенная разница в средней продолжительности одного звонка
между активными и потерянными клиентами?
"""
call_duration_by_churn = df.groupby('Churn')['Call_duration'].mean()
print(f'\n4. Средняя продолжительность звонка в каждой категории:\n{call_duration_by_churn}')


"""
5. Сгруппируйте данные по значению поля «Churn» и вычислите среднее
количество звонков в службу поддержки в каждой категории. Есть ли
существенная разница между активными и потерянными клиентами?
"""
service_calls_by_churn = df.groupby('Churn')['Customer service calls'].mean()
print(f'\n5. Среднее количество звонков в службу поддержки в каждой категории:\n{service_calls_by_churn}')


"""
6. Исследуйте подробнее связь между параметрами «Churn» и «Customer
service calls», построив таблицу сопряженности (факторную таблицу) по
этим признакам. Подсказка: используйте функцию crosstab. При каком
количестве звонков в службу поддержки процент оттока становится
существенно выше, чем в целом по датафрейму? (В качестве уточнения
фразы «существенно выше» можете использовать «более 40%».)
"""
CrossTab = pd.crosstab(df['Churn'], df['Customer service calls'])
Churn_By_Calls = CrossTab.apply(lambda x:x.iloc[1]/x.sum() * 100, axis = 0)

print(CrossTab)
Higher_Than_40 = Churn_By_Calls[Churn_By_Calls > 40]
print(f"\n6.  Количество звонков, при которых процент оттока выше 40%: \n{Higher_Than_40}")


"""
7. Аналогично предыдущему пункту исследуйте связь между
параметрами «Churn» и «International plan». Можно ли утверждать, что
процент оттока среди клиентов, использующих международный
роуминг, существенно выше или ниже, чем среди клиентов, не
использующих его?
"""
CrossTab_International = pd.crosstab(df['Churn'], df['International plan'])
Churn_By_International_Plan = CrossTab_International.apply(lambda x: x.iloc[1] / x.sum() * 100, axis=0)
No_International_Plan = Churn_By_International_Plan.get('No', 0)
International_Plan = Churn_By_International_Plan.get('Yes', 0)
print(f"\n7.  Процент оттока среди клиентов без международного плана: {No_International_Plan}%")
print(f"    Процент оттока среди клиентов с международным планом: {International_Plan:}%")


"""
8. Добавьте в датафрейм столбец «Прогнозируемый отток», заполнив его
на основе значений столбцов «Customer service calls» и «International plan».
Сравните значение в этом столбце со значением столбца «Churn». Если
мы будем пользоваться построенным прогнозом, то какой процент
ошибок первого и второго рода
(ложноположительных и
ложноотрицательных) мы получим?
"""
df['Projected outflow'] = ((df['Customer service calls'] > 3) | (df['International plan'] == 'Yes')).astype(int)

# Ложноположительные (ошибка первого рода): предсказали отток (1), но клиент не ушел (0)
Frame_Positive = ((df['Projected outflow'] == 1) & (df['Churn'] == 0)).sum()

# Ложноотрицательные (ошибка второго рода): предсказали отсутствие оттока (0), но клиент ушел (1)
Frame_Negative = ((df['Projected outflow'] == 0) & (df['Churn'] == 1)).sum()

# Общее количество клиентов с оттоком (Churn == 1)
Total_Positive = (df['Churn'] == 1).sum()

# Общее количество клиентов без оттока (Churn == 0)
Total_Negative = (df['Churn'] == 0).sum()

# Шаг 3: Рассчитываем проценты ошибок
# Процент ошибок первого рода (Frame_Positive)
FramePositive_Percentage = Frame_Positive / (Total_Positive + Total_Negative) * 100

# Процент ошибок второго рода (Frame_Negative)
FrameNegative_Percentage = Frame_Negative / (Total_Negative + Total_Positive) * 100

# Выводим результаты
print(f"\n8.  Процент ошибок первого рода (ложноположительных): {FramePositive_Percentage}%")
print(f"    Процент ошибок второго рода (ложноотрицательных): {FrameNegative_Percentage}%")