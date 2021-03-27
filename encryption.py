#Author: Shanu Thakur-20070243037
#Program: Encryption
#Date Created: 27-Mar-2021

import sys
from time import sleep as sl
# input string ftom user
str=input("Enter a string: ")

#variables
iterator=0
length=len(str)
cipher=""

#while loop
while (iterator<length):
	#increementing one character post the index character using ascii ordering number
	data=chr(ord(str[iterator])+1)
	cipher+=data   #appending each character one by one
	iterator=iterator+1


#printing the Cipher generated
print("The Cipher is : ",cipher )

# decrytping the cipher
sl(5)
print("Decrypting.....................................")



#variables
iterator=0
length=len(cipher)
cipher2=""



#while loop
while (iterator<length):
        #increementing one character post the index character using ascii ordering nu>
        data=chr(ord(cipher[iterator])-1)
        cipher2+=data   #appending each character one by one
        iterator=iterator+1



#printing the Cipher generated
print("The decrypted cipher is : ",cipher2 )

