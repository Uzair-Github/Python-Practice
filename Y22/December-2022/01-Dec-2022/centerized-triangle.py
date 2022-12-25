rows = int(input("Enter number: "))
count=star_count=1

sym_gap = " "
sym_star = "*"
gap = rows-1
#the relation is make with gap and stars with the help of rows
#the 2 rows will have 1 gap each side
#the 3 rows will have 2 gaps each side

#each time 2 stars increases from both sides
#each time 1 row count increases
#each time 1 gap will be reduced from both sides

#gaps can be changed with dashes "-"
while rows>=count:
    #print ("The start counting that ends up when equal number: ",count)
    print (gap*sym_gap,star_count*sym_star,gap*sym_gap)
    count+=1
    star_count+=2
    gap-=1
