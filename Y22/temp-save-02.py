def solve (a):
    print(a)
    solve(a)
    print(a)

a = [1,3,5]
a = [2,4,6]
print(solve(a))