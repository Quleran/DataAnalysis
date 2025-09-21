x = int(input())
y = int(input())
hour = 8
minut = 0

time = x * 2 * y

hour += time // 60
minut += time % 60

print(hour)
print(minut)
