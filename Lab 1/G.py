def calc_detail(a, b, n):
    if b == 0:
        return n
    if b >= a:
        return 0
    if n == 0:
        return 0
    else:
        total = (a * n - b) // (a - b)
        return total


a = int(input())
b = int(input())
n = int(input())

print(calc_detail(a, b, n))