strt = int(input("Start from this number: "))
end = int(input("and end from this number: "))
num = strt
if num%2 != 0:
    num = num+1
while strt<=num and end>=num:
    print(num)
    num = num+2
