def find_min_number(n, s):
    if s < 1 or s > 9 * n:
        return "NO"

    digits = [0] * n

    digits[0] = 1
    remaining = s - 1


    for i in range(n - 1, 0, -1):
        if remaining <= 0:
            break
        add = min(remaining, 9 - digits[i])
        digits[i] += add
        remaining -= add

    if remaining > 0:
        digits[0] += remaining

    return ''.join(str(d) for d in digits)

n = int(input())
s = int(input())

result = find_min_number(n, s)
print(result)