#Date Created: 10-3-2021
#Author: Shanu Thakur- 20070243037
#Program: 2. Temperature conversion

temperature=int(input("Enter the temperature you want to convert:"))

print("=========================================================================")


units=input("What is your temperature unit is in Celsius or Fahrenheit: ")

if  units=="C":
    F=(9/5)*(temperature+32)
    print("The temperature in farenheit will be",F)


elif  units=="F":
    C = (5/9)*(temperature-32)
    print("The temperature in celsius will be",C)

else:
    print("Invalid temperature")
