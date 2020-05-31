n = input("enter number")
a = 0
b = 1
print("fibonacci series is:")
for i in range(n):
   print(a, ' ' )
   c = a + b
   a = b
   b = c
