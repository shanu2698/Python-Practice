#Author: Shanu Thakur-20070243037
#Program: print all even characters in user input string
#Date Created: 27-Mar-2021

#input string from user
str= input("Enter a String: ")


#variables
length=len(str)
iterator=0

#while loop
while iterator<length:
	#checking if the itertot/ index is even or not
	if(iterator%2)==0:
		print(str[iterator])
	#increement iterator
	iterator=iterator+1

