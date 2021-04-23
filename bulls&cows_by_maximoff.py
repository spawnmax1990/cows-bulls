import random

#  TODO Часть 1. Компьютер загадывает число
listNumbers = [random.randint(0, 9)]

while len(listNumbers) < 4:
    x = random.randint(0, 9)
    turnOff = False
    for i in range(0, len(listNumbers)):
        if listNumbers[i] == x:
            turnOff = True
    if not turnOff:
        listNumbers.append(x)
# print(listNumbers)

#  TODO Часть 2. Диалог с пользователем
#  + Ввод четырехзначного числа с клавиатуры (например, 0000 ... 1234 ... 9999)
#  + Компьютер должен вывести на экран количество совпадений элементов загаданного числа
#  и количество символов которые стоят на нужном месте
#  пример загаданное число 1234,  пользователь ввел 4321, Вывод: Совпадений 4, Стоят на нужном месте 0
#  пользователь ввел 1567, Вывод: Совпадений 1, стоят на своем месте 1
#  пользователь ввел 5678, Вывод: Совпадений 0, стоят на своем месте 0
#  Чтобы выйти из программы введи 0

turnOff = True
print("Компьютер загадар 4х-значное число, нужно его угадать.")
print("Введите exit для выхода")
# print("Введите help для вызова справки")

while turnOff:
    numberString = input("Введите число: ")
    listCompare = []
    cows = 0
    bulls = 0

    if len(numberString) != len(listNumbers) or numberString.isdigit() != True:  # проверка сколько цифр ввели
        if numberString == "exit":
            turnOff = False
        else:
            print("Нужно ввести четырехзначное число")
    # elif int(numberString) == 0:  # выключить игру
    #     turnOff = False
    elif len(numberString) == len(listNumbers):  # определяем сколько коров и быков
        for i in range(len(listNumbers)):
            listCompare.append(int(numberString[i]))
        for i in range(len(listNumbers)):  # коров
            # compare = listNumbers[i] in listCompare
            if listNumbers[i] in listCompare:
                cows += 1

        for i in range(len(listNumbers)):  # быков
            if listCompare[i] == listNumbers[i]:
                bulls += 1


        # print(listCompare)
        print(f"Коров: {cows} / Быков: {bulls}")
        print("====================")

        if listCompare == listNumbers:  # если совпало то победа
            print("Победа! Вы угадали число!")
            turnOff = False

#  TODO Just do it:
    # + сделать чтобы пользователь не мог вводить меньше или больше 4х символов
    # - нужно сравнить введенный тип данных, чтобы нельзя было вводить текст.
    # нужно сравнить введеное число с загаданным и выдать ответ
    # подсказка 7я строка
    # TODO REPLACE THIS SHIT
    # сделать help, exit, version, restart, top :-)
    # вывести за сколько попыток угадал число
    # top-3 игрока (ввести имя игрока)
    # цветной вывод (фон у коров/быков)
    # сделать чтобы бот угадывал твоё число
    # сделать игру на двоих, PvP нах

# print("Тубэ пизда ('^')")

# # Часть 1. Компьютер загадывает число
# generate_number: list[int] = [random.randint(0, 9)]  # создаем массив под загаданное число, загадываем первую цифру
#
# for i in range(1, len(generate_number)):  # загадываем оставшиеся цифры числа
#     compare = random.randint(0, 9)
#     print(compare)
#
#     if compare == generate_number[0]:  # нужно сделать так, чтобы цифры в числе не повторялись
#         compare += 1
#         print(f"+1 = {compare}")
#
#     generate_number.insert(i, compare)

print(f"Я загадал число: {listNumbers[0]}{listNumbers[1]}{listNumbers[2]}{listNumbers[3]}")
