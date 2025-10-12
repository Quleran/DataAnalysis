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
print(f'\n4. Самая большая продолжительность звонка:\n{df_sorted.head(10)}')


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
Higher_Than_40 = Churn_By_Calls[Churn_By_Calls > 40]
print(f"\n6.  Количество звонков, при которых процент оттока выше 40%: \n{Higher_Than_40}")