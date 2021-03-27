#Date created: 10 march 2021
#Author: Shanu Thakur - 20070243037
#Program: 5. Greatest nested - if

number1=int(input("Enter number 1: "))
number2=int(input("Enter number 2: "))
number3=int(input("Enter number 3: "))
print("Entered numbers are: ",'\n',number1,'\n',number2,'\n', number3)


print("==============================================================")
if (number1>number2):
	print("Largest number is: ", number1)
elif (number2>number3):
	print("Largest number is: ", number2)
elif (number3>number2):
	print("Largest number is: ", number3)
else:
	print("Largest number is: ", number1)

