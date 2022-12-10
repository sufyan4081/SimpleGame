import random
print("*** Welcome to my Guess the game *** ")
r = random.randint(1,10)
guesses = 0
User = None
while(r != User):
    try:
        User = int(input("Enter any number : "))
        guesses += 1

        if(r == User):
            print("Congrats you are win the game...")
        elif(r < User):
            print("You are losed plz enter smaller value.")
        elif(r > User):
            print("You are losed plz enter greater value.")
    except Exception as e:
        print("Enter valid value like interger value 1,2,3,etc..")

print(f"you are guesses : {guesses} times")

with open("hiscore.txt","r") as f:
    hs = int(f.read())

if(guesses<hs):
    print("you just broken the score")
    with open("hiscore.txt","w") as f:
         f.write(str(guesses))
