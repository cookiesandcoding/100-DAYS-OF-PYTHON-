import random



from higherlowerart import logo, vs

from darahigherlower import personalities_professions , followers 

def position (option)  :
  for i in range (0, len(personalities_professions)):
    if option== personalities_professions[i]:
      return i
    
def comparing_followers(a,b,c,d):
  if c is not None and d is not None :
     answer='A'if followers[c]>followers[d] else 'B'
     return answer 
def less_followers(a,b,c,d):
  if followers[c]<followers[d]:
    less = a
  else:
    less=b
  return less 

def game():
  print(logo)
  option_2=random.sample(personalities_professions,1)[0]
  score=0
  end_of_game=False
  i=0
  while not end_of_game :
    i+=1
    option_1=random.sample(personalities_professions,1)[0]
    if option_1!=option_2:
      print(f" A: {option_1}")
      print(vs)
      print(f" B: {option_2}")
      position_1=position(option_1)
      position_2=position(option_2)
      correct_answer=comparing_followers(option_1,option_2,position_1,position_2)
      answer_given=(input("Who has more followers ?-Type \'A\' or \'B\'\n" )).upper()
      option_2=less_followers(option_1,option_2,position_1,position_2)
      
      if answer_given == correct_answer :
        score=score+1
        print(f"You guessed it right , Current score = {score} \n")
      else :
        print("You guessed it wrong \n")
      if i==10:
        print(f"Your final score is {score}")
        end_of_game=True
    else:
      end_of_game =False 
      
    
game()  
