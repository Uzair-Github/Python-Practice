bridge = input(str("Enter your # and gaps and make a bridge: "))
print("Your bridge is: ", bridge)
len_bridge = len(bridge)
lis_bridge=[]
flag=True
for i in range (0,len_bridge):
    lis_bridge.append(bridge[i])
    i=+1
print(lis_bridge)
    for j in range (0,len_bridge):
        if lis_bridge[j])=="#":
            flag = True
            print(flag)
        else:
            flag = False
            print(flag)
        j=j+1
if flag == True :
    print("bridge is safe")
else:
    print("bridge is broken")
