str_1="3,5,7,11,14"
print ("length of string is: ",len(str_1)-1)

for i in range (0,len(str_1)):
    if list_1[i]==",":
        i+=1
        if str_1[i] == int and str_1[i+1] == int:
            #print(i)
            temp_str=str(str_1[i])+str(str_1[i+1])
            print(int(temp_str))
            i+=1
        else:
            print("else i: ",i)
            print("else function having list [", i, "] is", str_1[i])
            i+=1
    #if list_1[i] == int: #and list_1[i+1] == int:
        #print("List i is: ",list_1[i],"List i+1 is: ",list_1[i+1])
