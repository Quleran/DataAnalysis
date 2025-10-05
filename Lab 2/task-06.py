def main():
    with open('mbox.txt', 'r') as file:
        lines = file.readlines()

    # Словарь для подсчета количества писем от каждого автора
    email_counts = {}

    for line in lines:
        # Ищем строки, начинающиеся с "From "
        if line.startswith('From '):
            # Разделяем строку по пробелам
            parts = line.split()
            # Второй элемент (индекс 1) должен быть email-адресом
            if len(parts) > 1:
                email = parts[1]
                # Увеличиваем счетчик для этого email
                email_counts[email] = email_counts.get(email, 0) + 1

    # Находим автора с наибольшим количеством писем
    if email_counts:
        max_email = max(email_counts, key=email_counts.get)
        max_count = email_counts[max_email]

        print("Все адреса авторов и количество писем:")
        for email, count in email_counts.items():
            print(f"{email}: {count} писем")

        print(f"\nАвтор с наибольшим количеством писем:")
        print(f"{max_email}: {max_count} писем")
    else:
        print("Адреса авторов не найдены")


if __name__ == '__main__':
    main()