import random
def Check(comp,user):
    if(user==comp):
        print("It's a draw")
        return 0
    elif(comp==1 and user==3):
        print("You lose")
        return -1
    elif(comp==2 and user==1):
        print("You lose")
        return -1
    elif(comp==3 and user==2):
        print("You lose")
        return -1
    else:
        print("You win")    
        return 1
    

print('''Welcome to the SNAKE*GUN*WATER Game\n Press 1 for Snake\n Press 2 for Gun\n Press 3 for Water\n ''')

while True:
    c=input("Press y to continue or n to exit:")
    if(c=='y'):
        user=int(input("Enter your choice: "))
        comp=random.randint(1,3)
        print(f"Your choice :{user}")
        print(f"Computer's choice :{comp}")
        check = Check(comp,user)
    else:
      break
    

