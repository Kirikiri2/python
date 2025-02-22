# 4 задача
let = ["2127", "2232323", "h", "j", "j"]
new = []
maxx = 0
for i in let:
    if len(i) > maxx:
        maxx = len(i)
for i in let:
    if len(i) < maxx:
        while len(i) < maxx:
            i += "_"
        new.append(i)
    else:
        new.append(i)
print(new)