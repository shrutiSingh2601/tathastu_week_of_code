def prime(n):
    a = 2
    b = n // 2
    while b >= a :
              return False
    a += 1
    b = n // a
    return True

def palindrome(n):
    a = str(n)
    l = len(a)
    for i in range( l // 2):
               if a[i] != a[l-1-i]:
                     return False
    return True

def odd(n) :
    if n % 2 == 0:
         return False
return True

def even(n) :
    if n % 2 != 0:
         return False
return True

def armstrong(n):
      sum = 0
      temp = n
      while temp > 0 :
          digit = temp % 10
          sum += digit ** 3
          temp //= 10
      if num == sum:
           return True
      return False
 
x = input("enter number")
if(prime(x)):
    print("prime")
if(odd(x)):
    print("odd")
else:
    print("even")
if(palindrome(x)):
    print("palindrome")
if(armstrong(x)):
    print("armstrong")
    
