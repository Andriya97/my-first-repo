num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose operation: +  -  *  /  %  **  //")
op = input("Enter operator: ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
elif op == "%":
    result = num1 % num2
elif op == "**":  
    result = num1 ** num2
elif op == "//":   
    result = num1 // num2
else:
    result = "Invalid operator!"


print("Result:", result)

#challenge👇
""" 
Add features:
If the user enters / and the second number is 0, print: "Error: Division by zero is not allowed!"
If the operator is not one of the above, print: "Invalid operator!"
Bonus 🚀: Allow the user to keep using the calculator until they type "exit".
"""