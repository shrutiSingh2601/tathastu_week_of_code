n = input(" enter n")
for i in range(n):
    print((str(n-i) + "*") * (n-1-i) + str(n-i))
for i in range(n):
    print((str(i) + "*") * (i-1) + str(i))
