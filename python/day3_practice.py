# Exercise 1: Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even!")
else:
    print("Odd!")

# Exercise 2: Name Repeater
name = input("What’s your name? ")
for i in range(3):
    print("Hello", name)

# Exercise 3: Simple Calculator
x = int(input("First number: "))
y = int(input("Second number: "))
op = input("Choose (+, -, *, /): ")

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x / y)
else:
    print("Invalid operator.")

# Exercise 4: Guess the Number
import random

secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Correct!")
else:
    print("Nope, the number was", secret)