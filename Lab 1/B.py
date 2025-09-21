import math

x = int(input())
y = int(input())
n = int(input())

if x > n:
    print(1)

else:
    if (n - y) % (x - y) == 0:
        print(int((n - y) / (x - y) + 1))
    else:
        days = math.ceil((n - y) / (x - y))
        print(days)
