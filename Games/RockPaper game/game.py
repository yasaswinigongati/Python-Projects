import random
userchoice=int(input("enter userchoice: 0 as rock,1 as paper,2 as scissor"))
if(userchoice>=3 and userchoice<0):
    print("invalid")
else:
    computerchoice=random.randint(0,2)
    print("computer chose")
    print(computerchoice)
    if(userchoice==computerchoice):
        print("you draw")
    elif(userchoice==0 and computerchoice==2):
        print("you win")
    elif(userchoice==2 and computerchoice==0):
        print("you lose")
    elif(userchoice>computerchoice):
        print("you win")
    elif(computerchoice>userchoice):
        print("you lose")


