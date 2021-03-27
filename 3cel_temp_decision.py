#Date created: 10-03-2021
#Author: Shanu Thakur 20070243037
#program: 3. Temperature

temp= float(input("Enter a temperature in celsius:- "))
print("============================================================")


if (temp < -273.15):
    print("the temperature is invalid because it is below absolute zero.")
elif(temp == -273.15):
    print("the temperature is absolute 0 ")
elif(temp>= -273.15 and temp<=0):
    print("the temperature is below freezing")
elif(temp == 0):
    print("the temperature is at the freezing point")
elif(temp>0 and temp<100):
    print("the temperature is in the normal range.")
elif(temp== 100):
    print("the temperature is at the boiling point")
elif(temp > 100):
    print("the temperature is above the boiling point")

else:
    print("Enter a valid input")
    

 
    
