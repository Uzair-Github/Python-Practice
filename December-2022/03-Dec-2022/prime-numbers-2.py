#program prints prime number till the number entered by user
num = int(input("Enter ending number: "))
flag=False
store=3
while store<=num:
    if store>2:
        for i in range (2,store):
            if store%i==0:
                flag=True
                break
    if flag == False:
        print (store, "is prime")
    flag = False
    store+=1
