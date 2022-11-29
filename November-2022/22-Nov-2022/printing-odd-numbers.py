odd = int(input("Enter your number: "))

if odd/2==0:
    odd = odd-1
    while odd>=1:
        print(odd)
        odd -= 2

else:
    while odd >= 1:
        print(odd)
        odd -= 2