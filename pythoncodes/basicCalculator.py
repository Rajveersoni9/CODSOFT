
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

num1=a
num2=b

operator = input("Enter an operator (1,2,3,4,5 or +,-,*,/,%): ")
if operator == '1' or operator == '+':
    result = num1 + num2
    print('Addition:',result)


elif operator == '2' or operator == '-':
    result = num1 - num2
    print('Subtration:',result)


elif operator == '3' or operator == '*':
    result = num1 * num2
    print('Multiplication:',result)


elif operator == '4' or operator == '/':
    if num2 != 0:
        result = num1 / num2
        print('Division:',result)


    else:
        result = "Error: Division by zero"
elif operator == '5' or operator == '%':
    if num2 != 0:
        result = num1 % num2
        print('Remainder:',result)


    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"
