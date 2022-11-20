#Enter 2 number
num1 =int(input("Enter: "))
num2 =int(input("Enter: "))

print(type(num1))
#For Checking the syntax if working or not
num3 = num1*3
print (num3)

#Example int vs float start
num4 = num1/num2

#Number converted to float due to number after decimal point
print (num4)
print(type(num4))

#If converted to int, it will not show any number after decimal point
num4 = int(num4)
print (num4)
print(type(num4))
