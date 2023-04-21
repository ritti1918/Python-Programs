import math
def isPrime(num):
    if(num<=1):
       return False
    for i in range(2,n+1):
       if(num % i==0):
          return False
    else :
      return True
    
num=int(input("Enter number"))
n=math.floor(math.sqrt(num))
c=isPrime(num)
if(c==True):
   print("Prime")
else:
   print("Not Prime")