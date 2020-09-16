import random
import math

#a one line comment 
#comments are ignored by python 
"""
This is a multi-line comment 
Turns red instead of green 
"""

#variables store a value and also have a type 
x = 5 #x is assigned 5 
#data type of x is integer 
print(type(x))
x = 5.5 #floating point value (fractional)
print(type(x))
my_name= "Hunter" #string (sequence of char)
print(my_name)

"""
Operators: 
* multiplication
/ floating point division 
// integer division 
"""
print(5/2)
print(5//2)

#** exponent 
print(2**5)
#you can import math module 
#sqrt()pow()tan()
print(math.pow(2,5))

"""
#getting input from user
user_name = input("What is your name? ")
print("hi, " + user_name)

#for a numeric input typecast to int or float
user_number = int(input("What is your fav #? "))
print(type(user_number))
"""

#print formatting of decimal (float) numbers
#c style 
print("%.2f" % (math.pi))
#python style 
print("{:.2f}".format(math.pi))
#how to round a decimal number
pi_rounded = round(math.pi, 2)
print(pi_rounded)


#conditionals (if statements)
x = 5
if x == 5: 
    print("x is 5")
    #4 spaces denotes membership of a body (like {})
else :
    print("x is not 5") 
    #elif = else if 

#loops 
#while loop just like c++
for i in range (0,5,1):
    print(i)

#warm up task
"""
m = int(input("enter int: "))
n = int(input("enter int: "))
m = m + 5 
n = 3 + n
print("m =", m, "\nn =", n)
"""


#2,4,6,8,...40
for i in range(2, 42, 2):
    print (i, end=", ")
print(i+2)

#use help() to view the documentation for an identifier (print)
#help(print)

#loops are used to repeat a sequence of statments 
#while loop solution from above
while i <= 38:
    print(i, end=", ")
    #progress towards the bollean condition being false
    i += 2
print (i)

#more on for loops
#for item in sequence 
# body (sequence of statement to be repeated)

animals = ["pig", "dragon"]
for animal in animals:
    print(animal)

#string is a sequence of chars
my_str = "aardvark" 
for char in my_str:
    print(char)

#advanced loops
#you can nest loops 
#you can use a break statment for early exit from loop 

while True:
    user_input = input("Please enter a word (stop to quit): ")
    if user_input == "stop":
        break

#random numbers
#lets throw a 6-sided die
#import random ints

#random.randrange(start, stop) 
roll = random.randrange(0 + 6) + 1 #[1,6]
print(roll)

roll = random.randint(1, 6) #[1,6]
print(roll)

# functions
# a function is a name sequence of statments mostly used for reusability
# and for code organization 

#def Function_name (parameter list):
#   indented body of statments 

def sayHello():
    print("Hello")

#need to call the function to execute its body
sayHello()

#example 2:
def say(message):
    print(message)
say("hello")
say("goodbye")

#task 
def cArea(r):
    area = math.pi * pow(r, 2)
    print(area)

cArea(2)

def cArea2(r):
    area = math.pi * pow(r, 2)
    return area
result = cArea2(5.0)
print (result)

#example 4:
def cAreaAndCircum(r):
    area = math.pi * pow(r, 2)
    circumference = 2 * math.pi * random
    return area, circumference
result1, result2 = cAreaAndCircum(5.0)
print (result1, result2)

