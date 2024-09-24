import random 
from Randomword import word_list
chosen_word = random.choice(word_list) #random word generation 
from hangman_art import logo , stages 
print(logo)
print (" Welcome to the game ! Let's play " + "\n")
lives=6 #max lives =6
# function for replacing charcaters at specified position 
def replace_char_at_position(string, position, new_character):
 return string[:position] + new_character + string[position+1:]
#generating the fill in the blank 
a=""
l =len(chosen_word)
for i in range (0,l) :
    a+="_"
print ("The word is : " + "\n")
print (f"The word is of {l} letters") 
print(a + "\n")
new_string=a
end_of_game = False
while not end_of_game :
    guess = input("Guess a letter: ").lower()
    #Checking for if letter is in the word 
    for letter in chosen_word:
        if letter == guess :
              
              if chosen_word.count(guess)==1 : #for those letters that occur once 
                    position=chosen_word.index(guess)
                    new_string = replace_char_at_position(new_string, position, guess)
              else: #for those letters that occur more than one time 
                   pos_list=[]
                   length=len(chosen_word)
                   for i in range (0, length) : #generating a list with positions of the letter in the word that occurs more than one time 
                       if chosen_word[i] == guess :
                           pos_list.append(i)
                   
                   length2=len(pos_list) 
                   for i in range (0,length2):# replacing the positions inside the list with the guessed letter 
                       pos=int(pos_list[i])
                       new_string = replace_char_at_position(new_string, pos, guess)
    if guess not in chosen_word :
               print(stages[lives] + "\n")
               print (f"You guessed {guess} , that's not in the word , thus you lose a life "+ "\n" )
               lives=lives-1
               if lives==-1:
                  print("you lose" + "\n")
                  print(f"The word was : {chosen_word}")
                  end=True 
                  end_of_game=True
    print(new_string)
    if "_" not in new_string :
      print ("You win" +"\n") 
      end_of_game=True
