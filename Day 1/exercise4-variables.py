'''
Write a program that switches the values stored in the variables a and b.
Warning: Do not change the code on lines 7-13 and 19-24. 
Your program should work for different inputs. e.g. any value of a and b.
'''

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Option 1
x = a
a = b
b = x

# Option 2
a, b = b, a

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)