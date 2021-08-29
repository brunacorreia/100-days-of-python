'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have 
left if we live until 90 years old.
'''
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You currently have {days_left} days, {weeks_left} weeks, {months_left} months and {years_left} years left.")