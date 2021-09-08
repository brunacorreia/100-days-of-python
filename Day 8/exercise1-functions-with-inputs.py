# write a function using PARAMETERS and ARGUMENTS

def greet(name, location):
  print(f"Welcome, {name}.")
  weather = input(f"How's the weather at {location} atm?\n")
  print(f"{weather}? It seems a good time for a cup of coffee..")

# calling the function with KEYWORDS ARGUMENTS
greet(location = "Florianópolis", name = "Bruna")

'''
# calling the function with POSITIONAL ARGUMENTS
greet("Bruna", "Florianópolis")
'''



