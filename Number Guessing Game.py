import random 
print("Welcome to the number guessing game ")
print("You have to guess the number from 1 to 100 ")
def guess_number(turns) :
  guess=int(input("Guess the number"))
  while turns!=0:
    turns=turns-1
    if turns == 0 :
      print("You've run out of guesses, you lose.")
      print("Game ends")
      print(f"The number was {number}")
      break
    if guess > number : 
        print ("Too high")
        print(f"You have {turns} attempts remaining to guess the number\n")
        
    elif guess< number :
        print("Too low")
        print(f"You have {turns} attempts remaining to guess the number\n")
        
    else : 
        print("You guessed it right , you won")
        break
    guess=int(input("Guess again"))
  
choice = (input("Choose the level - easy or difficult \n")).lower()
numbers_list = list(range(1, 101))
number=random.choice(numbers_list)
if choice=="easy":
  print("You have 10 attempts remaining to guess the number ")
  guess_number(10) #turns =10
elif choice=="difficult":
  print("You have 5 attempts remaining to guess the number")
  guess_number(5) #turns= 5
else :
  print("Wrong choice entered")
