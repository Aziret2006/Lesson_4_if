# # компьютер гадает число
# num = "Think a number 1 to 5 press Enter"
#
# print(num)
#
# number = "The number more then 3?"
# a = input(" number is 1 (yes/no)").lower().strip()  # создаем переменную и спарашиваеm
#
# #Создаем if конструкцию
# if a == "yes":
#     print("Guessed!")
# else:
#     number = input("The number more then 3?")
#
# #тут мы спрашиваем это цифра 2
# b = input(" number is 2 (yes/no)").lower().strip()  #
#
# if b == "yes":
#     print("Guessed!")
#
# #тут мы спрашиваем это цифра 3
# c = input(" number is 3 (yes/no)").lower().strip()
#
# if c == "yes":
#     print("Guessed!")

print("Выберите число с 1 до 5")

ant = input("Число равно 3? (да/нет)").lower()  # Переменная

if ant == "нет":
    ant = input("Число больше 3? (да/нет)").lower()
    if ant == "да":
        ant = input("Число 4? (да/нет)").lower()
        if ant == "да":
            print("Guessed!")
        else:
            ant = input("Число 5? (да/нет)").lower()
            if ant == "да":
                print("Guessed!")
            else:
                print("Не может быть!")

    else:
        ant = input("Число 2? (да/нет)").lower()
        if ant == "да":
            print("Guessed!")
        else:
            ant = input("Число 1? (да/нет)").lower()
            if ant == "да":
                print("Guessed!")
            else:
                print("Не может быть!")
else:
    print("Guessed!")