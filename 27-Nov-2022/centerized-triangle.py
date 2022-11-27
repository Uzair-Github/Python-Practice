star_lim = int(input("Enter number: "))
print("Your no is: ", star_lim)
ach_lim = 0
ch_lim = star_lim+1
print(type(ach_lim))
sym = "*"
dash = " "
if star_lim > 0:
    while ach_lim <= star_lim:
        if ach_lim/2==0:
            #print("Printing if")
            ach_lim += 1
            #print("ach_lim:",ach_lim)
            ch_lim -= 1
            #print("ch_lim:",ch_lim)
            print(dash * ch_lim, sym * ach_lim, dash * ch_lim)
            #print ("dash",dash,"ch_lim",ch_lim,"sym",sym,"ach_lim",ach_lim,"dash",dash,"ch_lim",ch_lim)

        else:
            #print("Printing else")
            ach_lim += 2
            #print("ach_lim:",ach_lim)
            ch_lim -= 1
            #print("ch_lim:",ch_lim)
            print(dash * ch_lim, sym * ach_lim, dash * ch_lim)
            #print("dash", dash, "ch_lim", ch_lim, "sym", sym, "ach_lim", ach_lim, "dash", dash, "ch_lim", ch_lim)
else:
    print("Error")