lim_num = int(input("Enter a number: "))

print ("Number will be printed till:",lim_num)
init = 0
print (init)
init = 1
if lim_num<=0:
    lim_num = int(input("Wrong number, Enter a number: "))
else:
    while lim_num>=init:
        print (init)
        init = init+init
