def calci(num1, num2, op):
    if op in ('/', '%', '//') and num2 == 0:
        return "Division or modulus by zero is not allowed."
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "%":
        return num1 % num2
    elif op == "**":  
        return num1 ** num2
    elif op == "//":   
        return num1 // num2
    else:
        return "Invalid operator!"
    
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
print("Choose operation: +  -  *  /  %  **  //")
operator = input("Enter operator: ")

calci(number1, number2, operator)
print("Result:", calci(number1, number2, operator))

