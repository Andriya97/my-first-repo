### # Variables & Data Types
'''
- Challenge :
1. Creates variables for:
- model_name
- learning_rate
- epochs
- is_trained
'''
model_name = "ImageClassifier"
learning_rate = 0.001
epochs = 50 
is_trained = False

'''
2. Print each variable with its type.
'''
print(f"Model Name: {model_name}, Type: {type(model_name)}")
print(f"Learning Rate: {learning_rate}, Type: {type(learning_rate)}")   
print(f"Epochs: {epochs}, Type: {type(epochs)}")
print(f"Is Trained: {is_trained}, Type: {type(is_trained)}")

### # Operators
'''
-Challenge:
Write code that:
- Checks if a number is **even**
- Checks if it is **greater than 10**
'''
number = int(input("Enter a no. :"))
if number % 2 ==0:
    print("It's an even number.")
else:
    print("It's an odd number.")

if number > 10:
    print("The number is greater than 10.")
elif number == 10:
    print("The number is 10.")
else:
    print("The number is not greater than 10.")

### # Input & Output
'''
-Challenge 1
Write a program that:
- Takes two numbers from user
- Prints their sum, difference, product
---
-Challenge 2
Ask user for:
- Name
- Age
Print:
---
Hello <name>, you will be <age+1>next year
---
'''
num1 = int(input("Enter a no. :"))
num2 = int(input("Enter a no. :"))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))    
print(f"Hello {name}, you will be {age+1} next year")

### # Conditions (if / elif / else)
'''
-Challenge 1
Take a number from user and:
- Print `"Positive"`, `"Negative"`, or `"Zero"`
---
-Challenge 2
Ask for marks and print:
- A (90+)
- B (75 - 89)
- C (50 - 74)
- Fail (<50)
'''
number = int(input("Enter a no. :"))
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")

mark= int(input("Enter your mark ="))
if mark >= 90:
    print("Grade A")
elif mark >= 75 and  mark < 90:
    print("Grade B")
elif mark >= 50 and mark < 75:
    print("Grade C")    
else:
    print("Fail")

### # Loops (for, while)
'''
-Challenge 1
Print all **even numbers from 1 to 20**
---
- Challenge 2
Take a number from user and:
- Print its multiplication table (1 to 10)
'''
print("Even numbers from 1 to 20:")
for i in range(21):
    if i%2==0:
        print(i)

num = int(input("Enter a no. :"))
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

### # Functions 
'''
-Challenge 1
Write a function:
- takes a number
- returns `"Even"` or `"Odd"`
---
Challenge 2
Write a function:
- takes 3 numbers
- returns the **maximum**
(No built-in `max()`)
'''
def even_or_odd(a):
    if a%2==0:
        print("It's Even")
    else:
        print("It's Odd")   

num = int(input("Enter a no. :"))
even_or_odd(num)

def max_find(a, b, c):
    if a>b and a>c:
        print(f"The maximum is: {a}")
    elif b>a and b>c:
        print(f"The maximum is: {b}")   
    else:
        print(f"The maximum is: {c}")
        
num1 = int(input("Enter first no. :"))
num2 = int(input("Enter second no. :"))     
num3 = int(input("Enter third no. :"))
max_find(num1, num2, num3)