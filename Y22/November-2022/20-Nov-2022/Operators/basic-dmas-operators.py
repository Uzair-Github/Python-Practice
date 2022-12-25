#taking input numbers as int
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

#adding numbers
sum = num1 + num2
print (num1, "+", num2, "= ", sum)

#subtracting numbers
sub = num1 - num2
print (num1, "-", num2, "= ", sub)

#multiplying two numbers
mult = num1 * num2
print (num1, "*", num2, "= ", mult)

#dividing two numbers
div = num1 / num2
print (num1, "/", num2, "= ", div)

#Reminder of numbers
rem = num1 % num2
print (num1, "%",num2, "= ", rem)
print (num1, "/",num2, "= ", int(div))

#statement with dividing and reminder
print ("After dividing", num1, "to",num2, ", we get", int(div), "as a whole number and" , rem , "as a reminder")