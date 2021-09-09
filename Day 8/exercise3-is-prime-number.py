#Write your code below this line 👇
def prime_checker(number):
  times_divisible = 0
  for i in range(1, number+1):
    if number % i == 0:
      times_divisible += 1

  if times_divisible == 2:
    print(f"{n} is a prime number")
  elif times_divisible > 2:
    print(f"{n} is not a prime number")

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)