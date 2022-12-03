#program prints prime number form and till the number entered by user
num2 = int(input("Enter starting number: "))
num1 = int(input("Enter ending number: "))
flag=False
store=3
while store<=num1:
    if store>2:
        for i in range (2,store):
            if store%i==0:
                flag=True
                break
    if flag == False:
        if store>=num2:
            print (store, "is prime")
    flag = False
    store+=1
