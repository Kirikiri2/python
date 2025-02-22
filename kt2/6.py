# 6 задача
question = ["Как называется столица Франции?\n", "Сколько планет в Солнечной системе?\n", "Как называется жидкость, заполняющая глазное яблоко?\n"]
answer = ["Париж", "восемь", "Кровь"]

for i in range(len(question)):
    vvod = input(question[i])
    if vvod.lower() == answer[i].lower():
        print("верно!")
    else:
        print("ошибка")