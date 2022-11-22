#less than, greater than and equal to application
import math

x = 15
y = 100

if x<y:
    print (x , "is smaller than ", y)
elif x==y:
    print (x, "is equal to ", y)
else:
    print (x, "is greater than ", y)

#raise to power (2) application and underroot to power (2) application
a = 16
b = 2

print (a,"power to", b, "is " , a**b)
print (a,"underroot power to", b, "is " , math.sqrt(a))
