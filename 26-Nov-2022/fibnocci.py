lim_num = int(input("Enter a number: "))

print ("Number will be printed till:",lim_num)
init0 = 0
count = 0
init1 = 0
init2 = 1
if lim_num<=0:
    lim_num = int(input("Wrong number, Enter a number: "))
else:
    print("Your Fibnocci Series: ")
    print(init0)
    while lim_num>init0:
        init1 = init2
        init2 = init0
        init0 = init1+init2
        count +=1
        print (count, "Fibnocci: ",init0)