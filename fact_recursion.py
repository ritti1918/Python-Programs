
#factorial using recursion function
print("Welcome to find the factorial of a number")
def fact(num):
    if(num==1):
        return 1
    else:
        return num*fact(num-1)
num= int(input("Enter the number: "))
print(fact(num))
