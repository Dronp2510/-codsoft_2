# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    condition = True

    print("Operations of calculator:- ")
    print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) Exit")


    while condition:
        
        choice = input("Enter your choice[1,2,3,4,5]:- ")
        
        
        if choice != '5':
            print("Enter two numbers.")
            num1 = int(input("Enter first number:- "))
            num2 = int(input("Enter second number:- "))

            match choice:
                case '1':
                    sum = add(num1 , num2) 
                    print(sum)
                case '2':
                    diff = subtract(num1 , num2)
                    print(diff)
                case '3':
                    product = multiply(num1 , num2)
                    print(product)
                case '4':
                    div = divide(num1 , num2)
                    print(div)
                case _:
                    print("invalid choice")
        else:
            print("exiting the calculator.")
            condition = False

if __name__ == '__main__':
    print("Note , the subtraction operation works in order of numbers inputed.")
    print("Note , In the division operation,the first number input is the numerator.")
    calculator()