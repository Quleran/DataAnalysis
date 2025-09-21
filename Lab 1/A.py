n = int(input())
sm = 0
for i in range(1, n + 1):
    sm += (2 * i) / (i + 2)
print(round(sm, 3))