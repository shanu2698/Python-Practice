#Date Created: 10-3-2021
#Author: Shanu Thakur- 20070243037
#Program: 1. Centimeter conversion

centimeter=int(input("Enter a length in centimeters:"))
print("====================================================")


if centimeter<0 :
    print("It is an invalid entry")
else :
    print("The length in inches is:",centimeter/2.54)
