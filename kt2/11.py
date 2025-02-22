# 11 задача
lst = [17, 4, 7, 10, 11, 12]
num = int(input())
close = lst[0]
diffmin = abs(lst[0] - num)
for i in range(1, len(lst)):
    diff = abs(lst[i] - num)
    if diff < diffmin:
        diffmin = diff
        close = lst[i]
print(close)