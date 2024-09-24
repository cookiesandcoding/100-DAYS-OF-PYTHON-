print("Thank you for choosing Python Pizza Deliveries!")
size = input("Enter the size (in capital) S, M or L ? ")
  # What size pizza do you want? S, M, or L
add_pepperoni = input( " Do you want pepperoni(in capital) ? Y or N ")
  # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese(in capital) ? Y or N")
  # Do you want extra cheese? Y or N

if (size=='S'):
 if (add_pepperoni=='Y'):
   if(extra_cheese=='Y'):
     bill=15+2+1
   else:
     bill=15+2+0
 else:
   if(extra_cheese=='Y'):
     bill=15+0+1
   else:
     bill=15+0+0


elif(size=='M'):
 if (add_pepperoni=='Y'):
   if(extra_cheese=='Y'):
     bill=20+3+1
   else:
     bill=20+3+0
 else:
   if(extra_cheese=='Y'):
     bill=20+0+1
   else:
     bill=20+0+0


else:
 if (add_pepperoni=='Y'):
   if(extra_cheese=='Y'):
     bill=25+3+1
   else:
     bill=25+3+0
 else:
   if(extra_cheese=='Y'):
     bill=25+0+1
   else:
     bill=25+0+0

print (f"Your final bill is: ${bill}.")
   
