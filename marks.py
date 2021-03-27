#Author: Shanu Thakur: 20070243037
#Program: Highest marks from user entered inputs  using Dictionary
#Date Created: 26-Mar-2021
List={}
no_Courses=int(input("Enter the number of courses: "))


iterator=0

while iterator<no_Courses:
	sub=input("enter the subject: ")
	marks=float(input("enter the marks for " + sub + ":"))
	data={sub:marks}
	List.update(data)
	iterator=iterator+1


print(List)

print("You have highest marks in : " + max(List) + "i.e " +  )

