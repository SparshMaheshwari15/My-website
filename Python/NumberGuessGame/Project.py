import random
random_number=random.randint(1,100)
#print(random_number)
number_of_guess=0
user_guess=None
while user_guess!=random_number:
    user_guess=int(input("Enter your guess "))
    number_of_guess=number_of_guess+1
    if user_guess==random_number:
        print("Congo you guess it correct") 
        
    else:
        if user_guess>random_number:
            print("You guess it wrong")
            print("Enter a smaller number")
        else:
            print("You guess it wrong")
            print("Enter a bigger number")

        
        
print(f"You have completed the game with {number_of_guess}  number of guess")

with open("high score.txt","r") as f:
    highscore=int(f.read())
if (number_of_guess<highscore):
    print("You have broken the record")
    with open("high score.txt","w") as f:
        f.write(str(number_of_guess))
else:
    print("You have not broken the record")
    print(f"High score is {highscore}")