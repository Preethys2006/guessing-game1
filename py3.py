import random
guess=(1,10)
def guess_number():
    guess_number=random.randint(1,10)
attempts=0
print("welcome to guessing game!")
print("I'am thinking of number between 1 to 10.can you guess it?")
while guess:
    guess=input("Enter a number:")
guess=int(guess)
attempts+=1 
if guess<guess_number:
    print("too low,try again.")
elif guess>guess_number:
    print("too high,try again.")
else:
    print(f"conguratulations!you've guessed a number{guess_number}in{attempts}attempts.")
guess_number()    
