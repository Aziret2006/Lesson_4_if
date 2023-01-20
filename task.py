
# находит среднее число
number1=int(input("enter first number:"))

number2=int(input("enter second number:"))

number3=int(input("enter third number:"))

if number2 < number1 < number3 or number3 < number1 < number2:
    print("Average", number1)
elif number1 < number2 < number3 or number3 < number2 < number1:
    print("Average", number2)
elif number2 < number3 < number1 or number1 < number3 < number2:
    print("Average", number3)
else:
    print("There is no average!")

#
number1=int(input("enter first number:"))
#
number2=int(input("enter second number:"))

number3=int(input("enter third number:"))

averege = None

# if number1 > number3:
#     if number1 < number3:
#         averege = number1
#     else:
#         averege = number3
# elif number2 > number1:
#     if number2 > number1:
#         averege = number2
# elif number3 > number1:
#     if number3 < number2:
#         averege = number3
#     else:
#         averege = number3






















