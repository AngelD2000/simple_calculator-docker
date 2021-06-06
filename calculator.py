def add(x,y): 
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y): 
    return x * y
def divide(x,y):
    return x/y

if __name__ == "__main__":
    operation = input("add, subtract, multiply, divide\n")
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    num_return = 0
    if operation == "add": 
        num_return = add(num1,num2)
    elif operation == "subtract": 
        num_return = subtract(num1,num2)
    elif operation == "multiply": 
        num_return = multiply(num1,num2)
    else:
        num_return = divide(num1,num2)
    print("Calculatiing...")
    print("Answer is {}".format(num_return))