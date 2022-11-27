star_lim = int(input("Enter number: "))
print("Your no is: ", star_lim)
ach_lim = 1
print(type(ach_lim))
sym = "*"
dash = "-"
if star_lim > 0:
    while ach_lim <= star_lim:
        print (dash)
        ach_lim+=1
else:
    print("Error")