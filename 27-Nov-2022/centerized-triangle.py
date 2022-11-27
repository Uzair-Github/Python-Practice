star_rows = int(input("Enter number: "))
print("Your no is: ", star_rows)
save_row = star_rows
oppo_count = 1
sym = "*"
sym_mult=2
dash = "-"
dash_mult=star_rows-2
while save_row>=0:
    while dash_mult >=1:
        print(dash*dash_mult,sym*sym_mult,dash*dash_mult)
        dash_mult-2
        sym_mult+2
        save_row-=1