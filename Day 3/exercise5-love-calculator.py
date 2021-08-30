# You are going to write a program that tests the compatibility between two people.
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_combination = (name1 + name2).lower()
true_count = 0
love_count = 0
true_count += sum(map(name_combination.count, ['t','r','u','e']))
love_count += sum(map(name_combination.count, ['l','o','v','e']))

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")