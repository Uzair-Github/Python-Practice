star_lim = int(input("Enter a number below 20: "))
print ("Triangle will have",star_lim,"Stars's triangle")
x = "*"
ocount=0
space = "-"
gap = star_lim*space
if star_lim<=20:
    while ocount <= star_lim:
        print(gap,x*ocount,gap)
        ocount = ocount + 1

else:
    print("Error")