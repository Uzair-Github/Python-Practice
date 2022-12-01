num = int(input("Enter number: "))
flag=False
while num>2
if num>1:
    for i in range (2,num):
        if num%i==0:
            flag=True
            break
if flag == False:
    print ("its prime")
else:
    print("its not a prime")


