"""
Начинающий предприниматель Александр открыл свою
первую пиццерию. Для учета заказов он использует максимально простой
инструмент – записывает в блокнот информацию о дате заказа, названии
пиццы и стоимости заказа (стоимость одной и той же пиццы даже в один и тот
же день может быть разной – это зависит от дополнительных ингредиентов,
которые пожелал добавить клиент, но которые Александр в своем блокноте
никак не учитывает). По прошествии нескольких дней Александр хочет
извлечь из своих записей какую-нибудь полезную информацию. Напишите
программу, которая будет выводить:
а) список всех пицц с указанием, сколько раз их заказывали; список должен
быть отсортирован по убыванию количества заказов, то есть первой в списке
должна оказаться самая популярная пицца;
б) список всех дат с указанием суммарной стоимости проданных в этот день
пицц; список должен быть отсортирован хронологически;
в) информацию о самом дорогом заказе;
г) среднюю стоимость заказа (среднее арифметическое по всем заказам)
Формат входных и выходных данных определите самостоятельно.
"""

def allPizza(orders):
    pizza = {}
    for order in orders:
        pizza_name = order['name']
        if pizza_name in pizza:
            pizza[pizza_name] += 1
        else:
            pizza[pizza_name] = 1

    sorted_pizzas = sorted(pizza.items(), key=lambda x: x[1], reverse=True)
    print("\na) Список пицц по популярности:")
    for pizza, count in sorted_pizzas:
        print(f"{pizza}: {count} раз(а)")

def allData(orders):
    data_sales = {}
    for order in orders:
        date = order['data']
        cost = order['cost']
        if date in data_sales:
            data_sales[date] += cost
        else:
            data_sales[date] = cost

    sorted_dates = sorted(data_sales.keys())
    print("\nб) Суммарная стоимость по дням:")
    for date in sorted_dates:
        print(f"{date}: {data_sales[date]} руб.")


def mxCost(orders):
    mx = 0
    mx_order = {}
    for order in orders:
        if order['cost'] > mx:
            mx = order['cost']
            mx_order = order


    print(f"\nв) Самый дорогой заказ: \n{mx_order['data']} {mx_order['name']} {mx_order['cost']}")


def  averageCost(orders, n):
    cost = 0
    for order in orders:
        cost += order['cost']

    print(f"\nг) Средняя стоимость заказов: {cost / n}")

def main():
    n = 0
    while n <= 0:
        try:
            n = int(input('Введите количество заказов: '))
            if n <= 0:
                print("Ошибка: количество заказов должно быть положительным числом")
        except ValueError:
            print("Ошибка: введите целое число")

    print('\nВведите каждый заказ в формате: дата(ДД.ММ.ГГГГ) название_пиццы стоимость')

    orsers = []
    for _ in range(n):
        s = input().split()
        data = s[0]
        name = s[1]
        cost = int(s[2])

        order = {
            'data': data,
            'name': name,
            'cost': cost
        }

        orsers.append(order)

    allPizza(orsers)
    allData(orsers)
    mxCost(orsers)
    averageCost(orsers, n)

if __name__ == '__main__':
    main()