import math
from caesarcipherart import logo 
print (logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar_cipher_encrypt(code,shift):
  encrypted_code=""
  for letter in code :
      if letter==" ":
        encrypted_code+=" "
      else : 
        position=alphabet.index(letter)
        new_position=position+shift
        new_letter=alphabet[new_position]
        encrypted_code+=new_letter
  print("The encrypted string is :")
  print(encrypted_code)

def caesar_cipher_decrypt(code, shift ):   
  decrypted_code=""
  for letter in code :
    if letter==" ":
      decrypted_code+=" "
    else:
      position=alphabet.index(letter)
      new_position=position-shift
      new_letter=alphabet[new_position]
      decrypted_code+=new_letter
  print("The decrypted string is :")
  print(decrypted_code)
  
  
end =False  
while not end : 
  choice=(input("Type encode for encrypting and decode for decrypting \n")).lower()
  if choice== "encode":
    msg=(input("Type your message\n")).lower()
    shift_no=int(input("Type the shift number\n"))
    caesar_cipher_encrypt(msg,shift_no)
  if choice=="decode":
    msg=(input("Type your message\n")).lower()
    shift_no=int(input("Type the shift number\n"))
    caesar_cipher_decrypt(msg,shift_no)
  continue_or_not=(input("Type yes for continuing , and no to discontinue \n")).lower()
  
  if continue_or_not=="yes" :
    choice=(input("Type encode for encrypting and decode for decrypting \n")).lower()
    end=False 
  if continue_or_not=="no":
    print("The task ends\n  ")
    end=True 
  
  
