n = int(input())
count = n
flag = False

while not(flag):
    if len(str(count)) == len(set(str(count))):
        flag = True
    else:
        count -= 1

print(count)