star_lim = int(input("Enter a number below 20: "))
print ("Triangle will have",star_lim,"Stars's triangle")
x = "*"
ocount=0
if star_lim<=20:
    while ocount<=star_lim:
        print(x*ocount)
        ocount=ocount+1
else:
    print("Error")