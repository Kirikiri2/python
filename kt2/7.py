# 7 задача
point = {
    1: 'AEIOULNSTR',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JZ',
    10: 'QZ'
}
stroka = input().upper()
count = 0
for i in stroka:
    for value, bukva in point.items():
        if i in bukva:
            count += value
print(count)