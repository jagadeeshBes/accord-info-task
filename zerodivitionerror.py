try:
    num1 = int(input("enter number"))
    num2 = int(input("enter number"))
    div = num1/num2
    print("divide number",div)
except ZeroDivisionError:
    print("cant divide a number by zero")
        