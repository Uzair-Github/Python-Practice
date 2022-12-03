num = int(input("Enter number: "))
flag=False

if num>1:
    for i in range (2,num):
        if num%i==0:
            flag=True
            break
if flag == False:
    print ("its prime")
else:
    print("its not a prime")
#num = int(input("Enter number: "))
#count=0
#for i in range (2,num):
    #if num%i==0:
        #count =count+1
        #break
#if count == 0:
    #print("Its a prime", i, num)
#else:
    #print("Its not prime", i, num)

