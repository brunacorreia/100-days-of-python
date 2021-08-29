'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.

Warning you should round the result to the nearest whole number. 
The interpretation message needs to include the words in bold from the interpretations above. 
e.g. **underweight, normal weight, overweight, obese, clinically obese.**
'''

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bodymass_index = round(weight // height**2)

print(f"Your Body Mass Index is {bodymass_index}")
if bodymass_index <= 18.5:
    print("According to your Body Mass Index (BMI), you are **overweight**.")
elif bodymass_index > 18.5 and bodymass_index < 25:
    print("According to your Body Mass Index (BMI), you have **normal weight**.")
elif bodymass_index > 25 and bodymass_index < 30:
    print("According to your Body Mass Index (BMI), you are **slightly overweight**.")
elif bodymass_index > 30 and bodymass_index < 35:
    print("According to your Body Mass Index (BMI), you are **obese**.")
else:
    print("According to your Body Mass Index (BMI), you are **clinically obese**.")