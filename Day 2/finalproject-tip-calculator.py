total_bill = float(input("Welcome to the Tip Calculator!\nWhat was the total bill?\n$ "))
tip_tax = int(input("How much tip would you like to give?\n>10\n>12\n>1\n"))
people_sharing = int(input("How many people are able to split the bill?\n"))
tip_tax = tip_tax/100
per_person = (total_bill*(tip_tax + 1))/ people_sharing
result = round(per_person, 2)
print(f"Each person should pay: $ {result}.")