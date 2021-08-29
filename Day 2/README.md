# Day 2 Summary

## Python Primitive Data Types
- String
- Integer
- Float
- Boolean

## Functions
- len(var) -> The len() function does not work for numbers. Only object of type 'str'.
- type(var) -> Shows the type of the variable

## Mathematical Operators
| Sign | Operation |
| --- | --- |
| `+` | addition |
| `-` | subtraction |
| `*` | multiplication |
| `/` | division |
| `//` | floor (division returning an integer) |
| `%` | modulus (division remainder)
| `**` | exponent |
| `-` | subtraction |

## Operations Priority
**PEMDAS (left to the right):**
1. Parentheses `()`
2. Exponents `**`
3. Multiplication `*` = Division `/`
5. Addition `+` = Subtraction `-`

**e.g.** <br>
print(3 * (3 + 3) / 3 - 3) -> 3
print(3 * 3 + 3 / 3 - 3) -> 7

### Avoiding repetitive operations
- variable += 1
- variable -= 1
- variable *= 1
- variable /= 1

## F-String
score = 0
height = 1.8
isWinning = True

e.g. **print(f"Your current score is {score}, your height is {height}, you are winning is {isWinning}")**

## Annotations
### Subscripting
The method of pulling out a particular element from a string.
- e.g. print("Hello"[0]) -> "H"

### Variables
- It is possible to add the underscore into a number to make a large number more readable. It does not affect the output.<br>e.g. mystery = 734_529.678<br>print(mystery)<br>type(mystery)<br>734529.678<br>Float

#### Functions
String conversion:
- str(var)
- int(var)
- float(var)
To round a number to a given precision in decimal digits:
- round(var, 2)
To round a number to a integer:
- round(var)
- int(var)
- x // y





