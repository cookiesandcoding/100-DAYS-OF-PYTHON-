#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
p=''
q=''
r=''
#choices() function returns a list of random elements from the string or list you give it 
# we have applied str function so that every element in the list is converted to string 
# thus every string in then concatenated to form a single string 
total=nr_letters+nr_numbers+nr_symbols
for i in range (0,nr_letters):
  p+=str((random.choice(letters)))
for i in range (0,nr_numbers):
  q+=str((random.choice(numbers)))
for i in range (0,nr_symbols):
  r+=str((random.choice(symbols)))
s=p+q+r #combines the letter , numbers and symbols 
t=len(s)
u=[]
for i in range (0,t):#converts the string s into a list in order to shuffle it because shuffle can be applied to a list not to a string 
  u.append(s[i])
random.shuffle(u)# shuffles the list u 
v=" "
for i in range (0,t) : #converts the list u into a string v 
 v+=u[i]
print(v)

