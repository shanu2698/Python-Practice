#Date Created: 10-3-2001
#Author: Shanu Thakur 20070243037
#Program: 4. Accept age and use nested if else and print....


age=int(input("Please enter your age: "))
print("==========================================================")


if (age<0):
	print("The Entered Age is Invalid!!!!")
elif(age <= 18):
	print("Message: You are minor and you are not eligible to work!")
elif(age>=18) and (age<=60):
	print("Message: You are eligible to work!! Fill your details and apply.")
else:
	print("Message: You are too old to work, collect your pension :(")
