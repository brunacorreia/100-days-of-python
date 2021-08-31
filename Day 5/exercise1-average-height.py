'''
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

Example of output expected:
There are a total of 7 heights in student_heights
Average height rounded to the nearest whole number = 164

**Important You should not use the sum() or len() functions in your answer. 
You should try to replicate their functionality using what you have learnt about for loops.**
'''
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights, in centimeters ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total_height = 0
for i in student_heights:
    total_height += i
total_height = round(total_height/100, 2)
print(total_height)

total_students = 0
for i in student_heights:
    total_students += 1
print(total_students)

average_height = round(total_height / total_students, 2)

print(f"There are {total_students} students and their average height is {average_height}.")