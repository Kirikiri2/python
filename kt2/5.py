# 5 задача
mark = [4,3,2,5]
filtmark = []
i = 0
while i < len(mark):
    if (mark[i] == 2) and ((i + 1 < len(mark)) and (mark[i + 1] != 2)):
        i += 1
    else:
        filtmark.append(mark[i])
    i += 1
if not filtmark:
    print(2)
else:
    result = sum(filtmark) / len(filtmark)
    print(round(result))