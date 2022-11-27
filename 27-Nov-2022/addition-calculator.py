n = int(input("Enter Number to calculate sum: "))
#error checker print("Added: ",n)
num = 0
#error checker print("Num set:",num)
while n != 0:
    num += n
    #error checker print("Loop n:", n)
    #error checker print("Loop num:",num)
    n = int(input("Enter a number or just hit 0 to quit: "))
    #error checker print ("Loop end n:", n)
    #error checker print("Loop end num:", num)

print("The sum is", num)