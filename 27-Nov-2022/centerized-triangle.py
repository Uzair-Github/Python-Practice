star_rows = int(input("Enter number: "))
print("Your no is: ", star_rows)
sym_mult = 0
dash_mult = star_rows+1
print(type(sym_mult))
sym = "*"
dash = "-"
if star_rows > 0:
    while sym_mult <= star_rows:
        if sym_mult/2==0:
            print("Printing if")
            sym_mult += 1
            #print("sym_mult:",sym_mult)
            dash_mult -= 1
            #print("dash_mult:",dash_mult)
            print(dash * dash_mult, sym * sym_mult, dash * dash_mult)
            print ("dash:",dash,"dash_mult:",dash_mult,"sym:",sym,"sym_mult:",sym_mult,"dash:",dash,"dash_mult:",dash_mult)

        else:
            print("Printing else")
            sym_mult += 2
            #print("sym_mult:",sym_mult)
            dash_mult -= 1
            #print("dash_mult:",dash_mult)
            print(dash * dash_mult, sym * sym_mult, dash * dash_mult)
            print ("dash:",dash,"dash_mult:",dash_mult,"sym:",sym,"sym_mult:",sym_mult,"dash:",dash,"dash_mult:",dash_mult)
else:
    print("Error")