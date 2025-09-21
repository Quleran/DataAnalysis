x = int(input())
y = int(input())

total = 0
days = 0

while total < y:
    days += 1
    total += days * (x + 2 * (days - 1))
print(days)