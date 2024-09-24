print ("Welcome to hiding treasure")

line1 = ["⬜️","⬜️","⬜️"]
line2 = ["⬜️","⬜️","⬜️"]
line3 = ["⬜️","⬜️","⬜️"]
map = [line1, line2, line3]
print("   A      B      C")
print(f"{1}{line1}\n{2}{line2}\n{3}{line3}")


column=input("Enter the column (in capital )- A, B or C\n")
row=input("Enter the row - 1, 2 or 3\n")
position = column + row
print("The position asked for hiding the treasure is :" + position + "\n")
print("Hiding your treasure! X marks the spot.\n")

if (position[1]=='1'):
  if(position[0]=='A'):
    map[0].pop(0)
    map[0].insert(0 ,'X' )
    print(f"{line1}\n{line2}\n{line3}")
  elif(position[0]=='B'):
    map[0].pop(1)
    map[0].insert(1,'X' )
    print(f"{line1}\n{line2}\n{line3}")
  else:
    map[0].pop(2)
    map[0].insert(2,'X' )
    print(f"{line1}\n{line2}\n{line3}")
    
    
elif (position[1]=='2'):
  if(position[0]=='A'):
     map[1].pop(0)
     map[1].insert(0 ,'X' )
     print(f"{line1}\n{line2}\n{line3}")
  elif(position[0]=='B'):
     map[1].pop(1)
     map[1].insert(1 ,'X' )
     print(f"{line1}\n{line2}\n{line3}")
  else:
     map[1].pop(2)
     map[1].insert(2 ,'X' )
     print(f"{line1}\n{line2}\n{line3}")
    
else:
  if(position[0]=='A'):
    map[2].pop(0)
    map[2].insert(0 ,'X' )
    print(f"{line1}\n{line2}\n{line3}")
  elif(position[0]=='B'):
    map[2].pop(1)
    map[2].insert(1 ,'X' )
    print(f"{line1}\n{line2}\n{line3}")
  else:
    map[2].pop(2)
    map[2].insert(2 ,'X' )
    print(f"{line1}\n{line2}\n{line3}")
