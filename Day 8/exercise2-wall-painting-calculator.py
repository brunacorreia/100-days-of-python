'''
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
'''
import math

print("Welcome to the WALL PAINTING CALCULATOR.\n")
paint_coverage = float(input("Paint coverage [m²/coat]: "))
coats_number = float(input("Number of Coats: "))
wall_height = float(input("Wall Height: "))
wall_width = float(input("Wall Width: "))
total_area = 0
sum_walls = True

while sum_walls == True:
  
  def area_calc():
    wall_area = wall_height * wall_width
    return wall_area
  wall_area = area_calc()
  total_area += wall_area
  add_wall = input("Is there any other wall you'd like to paint? Y/N\n").lower()

  if add_wall == "y":
    wall_height = float(input("Wall Height: "))
    wall_width = float(input("Wall Width: "))
    area_calc()
  else:
    sum_walls == False
    print(f"Your total area is: {total_area} m².")
    paint_coverage = paint_coverage / coats_number
    cans = math.ceil(total_area / paint_coverage)
    print(f"You will need {cans} cans of paint.")
    break

'''
def paint_calc(height, width, cover):
  cans = math.ceil(test_h * test_w / coverage)
  print(f"You will need {cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
'''