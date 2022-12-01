rows = int(input("Enter number: "))
count=star_count=1

sym_gap = " "
sym_star = "*"
gap = rows-1

while rows>=count:
    #print ("The start counting that ends up when equal number: ",count)
    print (gap*sym_gap,star_count*sym_star,gap*sym_gap)
    count+=1
    star_count+=2
    gap-=1
