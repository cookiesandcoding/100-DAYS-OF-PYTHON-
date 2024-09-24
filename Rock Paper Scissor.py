import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice=int(input("Enter 0 for rock , 1 for paper and 2 for scissors"))
comp_choice=random.randint(0,2)
print(f"User\'s choice = {game_images[user_choice]}" )
print(f"Computer\'s choice =\n {game_images[comp_choice]}")
if(user_choice==0 and comp_choice==2)or (user_choice==1 and comp_choice==0)or(user_choice==2 and comp_choice==1):
 print ("You win")
else :
 print("You lose")
                
