number = int(input("Enter an odd or even number: "))
if number % 2 == 0: 
    print("The number is even")
else:
    print("The number is odd")


name = input("Enter you're name: ")
for i in range(5):
    print("Hello " + name)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Choose (+, -, *, /): ")

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x / y)


import random
num = random.randint(1, 10)
guess = int(input("Guess random number 1 to 10: "))

if guess == num:
    print("correct")
else: 
    print("wrong")


