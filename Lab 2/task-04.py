def main():
    # Чтение входных данных
    names = input().split()
    n = int(input())

    # Словарь для хранения расходов каждого участника
    expenses = {name: 0 for name in names}

    # Чтение информации о покупках
    for _ in range(n):
        name, amount = input().split()
        expenses[name] += int(amount)

    # Расчет средней суммы
    total_expenses = sum(expenses.values())
    average = total_expenses / len(names)

    # Определение должников и кредиторов
    creditors = []  # Те, кто потратил меньше среднего (должны получить деньги)
    debtors = []  # Те, кто потратил больше среднего (должны отдать деньги)

    for name in names:
        balance = expenses[name] - average
        if balance < -0.01:  # Потратил меньше среднего (нужно получить)
            creditors.append((name, -balance))
        elif balance > 0.01:  # Потратил больше среднего (нужно отдать)
            debtors.append((name, balance))

    # Сортируем по убыванию суммы долга/кредита
    creditors.sort(key=lambda x: x[1], reverse=True)
    debtors.sort(key=lambda x: x[1], reverse=True)

    # Выполняем переводы с минимальным количеством операций
    transfers = []
    i, j = 0, 0

    while i < len(creditors) and j < len(debtors):
        creditor, credit_amount = creditors[i]
        debtor, debt_amount = debtors[j]

        # Сумма перевода - минимальная из двух сумм
        transfer_amount = min(credit_amount, debt_amount)

        # Округляем до 2 знаков после запятой
        transfer_amount = round(transfer_amount, 2)

        if transfer_amount > 0.01:  # Игнорируем очень маленькие суммы
            transfers.append((debtor, creditor, transfer_amount))

            # Обновляем оставшиеся суммы
            creditors[i] = (creditor, credit_amount - transfer_amount)
            debtors[j] = (debtor, debt_amount - transfer_amount)

            # Если кредит погашен, переходим к следующему кредитору
            if creditors[i][1] < 0.01:
                i += 1

            # Если долг погашен, переходим к следующему должнику
            if debtors[j][1] < 0.01:
                j += 1

    # Вывод результатов
    print(len(transfers))
    for debtor, creditor, amount in transfers:
        print(f"{debtor} {creditor} {amount:.2f}")


if __name__ == "__main__":
    main()
