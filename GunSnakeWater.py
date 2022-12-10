import random

def myFunc(User,Comp):
    if(User == Comp):
        print("Match is draw...")
    elif(User == "gun" and Comp == "snake" or User =="sanke" and Comp =="water" or User =="water" and Comp == "gun"):
        print("User win!")
    else:
        print("Computer win!")


User = (input("slecte any one : (gun) (snake) (water) : "))
randNo = random.randint(1,3)
if randNo == 1:
    Comp = "gun"
elif randNo == 2:
    Comp = "snake"
elif randNo == 3:
    Comp = "water"

print(f"Computer selected {Comp}")
print(f"User selected {User}")
myFunc(User,Comp)