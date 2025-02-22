# 12 задача
string = input()
start = input()
end = input()
start_i = string.index(start) + 1
end_i = string.index(end)
print(string[start_i : end_i])