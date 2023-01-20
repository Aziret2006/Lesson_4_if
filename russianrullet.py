from random import randint


result = randint(1, 7)# от 1 до 7 рандомизатор

choice = int(input("Enter num 1 to 7:"))

if 1 <= choice <= 7:
	if choice != result:
		print("You lucky, was an unlucky number:", result)
	else:
		print("You dead")
else:
	print("1 to 7")
