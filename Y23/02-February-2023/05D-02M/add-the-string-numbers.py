str_1 = "3,5,7,11,14"
len_str = len(str_1)
print("length of string is: ", len_str - 1)

for i in range(0, len_str):
    try:
        # print(i)
        x = int(str(str_1[i]) + str(str_1[i + 1]))
        print("x:", x)

    except ValueError:
        # print(i)
        if str_1[i] != ",":
            x = int(str_1[i])
            print("x:", x)