"""
Компания друзей собралась пойти в поход. Забот и затрат
при подготовке похода оказалось много: кто-то закупал еду, кто-то брал в
аренду снаряжение, кто-то заказывал транспорт. Когда всё было готово, друзья
решили подсчитать, кто сколько денег потратил и, соответственно, кто кому
сколько денег должен перевести. Статей расходов оказалось очень много,
участников похода было тоже много, поэтому сделать все расчеты вручную
оказалось затруднительно.
Напишите программу, которая по информации о том, кто сколько денег
потратил, определит: кто, кому и сколько денег должен перевести, чтобы
расходы всех участников похода оказались одинаковыми (с точностью до
копейки). Количество переводов при этом должно быть как можно меньше.

ВХОДНЫЕ ДАННЫЕ
В первой строке через пробел записаны имена всех участников похода.
Имена уникальны, каждое имя состоит из латинских букв. Длина каждого
имени – не более 20 символов, количество имен – не более 100
Во второй строке записано одно целое число N – количество покупок,
которое было сделано при подготовке похода.
Далее следует N строк, каждая из которых описывает одну покупку и
содержит имя того, кто эту покупку оплачивал, и одно целое число – сумму
покупки. Имя и число разделены пробелом. Гарантируется, что имя есть в
общем списке участников похода.

ВЫХОДНЫЕ ДАННЫЕ
В первой строке выведите одно число M – минимальное количество
переводов, которые нужно совершить.
Далее выведите M строк, в каждой указав два имени и вещественное число
через пробел: кто, кому и сколько должен перевести. Все суммы переводов
должны быть округлены до 2 знаков после запятой. Если существует несколько
вариантов переводов, то выведите любой из них – главное, чтобы их количество
было минимальным.
"""

def main():
    # Имена всех участников похода
    names = input().split()

    # Количество покупок
    n = int(input())

    # Словарь, ключ - имя участника, значение - сумма его расходов
    expenses = {}
    for name in names:
        expenses[name] = 0

    for _ in range(n):
        data = input().split()
        buyer = data[0]
        amount = int(data[1])
        expenses[buyer] += amount


    total_expenses = sum(expenses.values())  # Общая сумма всех расходов
    average_expense = total_expenses / len(names)  # Средняя сумма на человека

    print(f"Общие расходы: {total_expenses}")
    print(f"Средняя сумма на человека: {average_expense:.2f}")

    # Баланс = потрачено - средняя сумма
    balances = {}
    for name in names:
        balance = expenses[name] - average_expense
        balances[name] = balance
        print(f"{name}: потратил {expenses[name]}, баланс: {balance:.2f}")

    debtors = []  # Те, кто должен деньги (отрицательный баланс)
    creditors = []  # Те, кому должны деньги (положительный баланс)

    for name, balance in balances.items():
        # Используем погрешность 0.001 для учета ошибок округления
        if balance < -0.001:  # Должник
            debtors.append((name, balance))
        elif balance > 0.001:  # Кредитор
            creditors.append((name, balance))

    print(f"\nДолжники: {debtors}")
    print(f"Кредиторы: {creditors}")

    debtors.sort(key=lambda x: x[1])
    creditors.sort(key=lambda x: -x[1])

    print(f"\nПосле сортировки:")
    print(f"Должники: {debtors}")
    print(f"Кредиторы: {creditors}")


    transfers = []

    i = 0  # Указатель на текущего должника
    j = 0  # Указатель на текущего кредитора

    while i < len(debtors) and j < len(creditors):
        debtor_name, debtor_balance = debtors[i]
        creditor_name, creditor_balance = creditors[j]

        transfer_amount = min(-debtor_balance, creditor_balance)
        transfers.append((debtor_name, creditor_name, transfer_amount))

        print(f"\nПеревод: {debtor_name} -> {creditor_name}: {transfer_amount:.2f}")

        debtor_balance += transfer_amount  # Должник отдает деньги
        creditor_balance -= transfer_amount  # Кредитор получает деньги

        # Обновляем значения в списках
        debtors[i] = (debtor_name, debtor_balance)
        creditors[j] = (creditor_name, creditor_balance)

        print(f"После перевода:")
        print(f"  {debtor_name} остался должен: {-debtor_balance:.2f}")
        print(f"  {creditor_name} осталось получить: {creditor_balance:.2f}")

        # Переходим к следующему участнику, если его баланс близок к нулю
        if abs(debtor_balance) < 0.001:  # Должник полностью рассчитался
            i += 1
            print(f"  {debtor_name} полностью рассчитался")

        if abs(creditor_balance) < 0.001:  # Кредитор получил все деньги
            j += 1
            print(f"  {creditor_name} получил все деньги")


    print(f"\n=== РЕЗУЛЬТАТ ===")
    print(len(transfers))
    for debtor, creditor, amount in transfers:
        print(f"{debtor} {creditor} {amount:.2f}")


if __name__ == "__main__":
    main()