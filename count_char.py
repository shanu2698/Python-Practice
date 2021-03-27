#Author: Shanu Thakur- 20070243037
#Program: Count number of charcater in a string
#Date: 26-Mar-2021

#method 1
print("xxxxxxxxx 1st way xxxxxxxxxxx")
#string
str="qhksgxjqhgbxkhb#@%$%&^(*&*BJHVHGV&*^&*%$$$$$$$^&*&(U()*"
no_of_count=str.count("$")
print(no_of_count)


#method 2
print("xxxxxxxxxxx 2nd way xxxxxxxxxxxxx")
#declare variables
str=input("Enter a String: ")
no_of_count=0
iterator=0

# length of string
length=len(str)

# parsing until every single character in the string
while iterator<length:
	if (str[iterator]=="$"):
		# while parsing if '$' is found  we increement the count
		no_of_count=no_of_count+1
	#increementing the iterator
	iterator=iterator+1

#printing the output
print("Total no of $ is : ", no_of_count)
