# # SNAKE WATER GUN
'''
     Sanke = -1
     Water = 0
     Gun = 1
'''

import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {"s":-1 , "w":0, "g":1}
revdict = {-1:"snake" , 0:"water", 1:"gun"}
you = youdict.get(youstr)


if you is None:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    print(f"your choice is {revdict[you]} \ncomputer choice is {revdict[computer]}")
    if(computer == you):
        print("Match draw")
    else:
        if computer==-1 and you==0:
            print("You Lose!")
        elif computer==-1 and you==1:
            print("You Win!")
        elif computer==0 and you==-1:
            print("You Win!")
        elif computer==0 and you==1:
            print("You Lose!")
        elif computer==1 and you==0:
            print("You Win!")
        elif computer==1 and you==-1:
            print("You Lose!")
        else:
            print("something went wrong")
