# Enter your height in meters e.g., 1.55m
height = float(input("Enter your height"))
# Enter your weight in kilograms e.g., 72kg
weight = int(input("Enter your weight"))

bmi=weight/(height**2)
if bmi<18.5 :
 print(f"Your BMI is {bmi} kg/m^2, you are underweight.")

elif  (bmi<25) :
 print(f"Your BMI is {bmi} kg/m^2, you have a normal weight.")

elif (bmi<30) :
 print(f"Your BMI is {bmi} kg/m^2, you are slightly overweight.")

elif (bmi<35) :
 print(f"Your BMI is {bmi} kg/m^2, you are obese.")

else :
 print(f"Your BMI is {bmi} kg/m^2, you are clinically obese.")
