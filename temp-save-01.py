num = int(input("Enter number: "))
flag=False

if num>1:
    for i in range (2,num):
        if num%i==0:
            flag=True
            break
    if flag == False:
        print(num, "is prime")
    else:
        print(num, "is not prime")