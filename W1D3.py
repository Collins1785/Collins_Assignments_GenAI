#Week1 - Day3 Assignment Calculator: Add, Sub, Divide, Multiply, Sqrt
while True:
    #Get user input for operation
    z=str(input("Enter the operation to perform calculation (+, -, /, *, sqrt) \n or type 'exit' to come out of the calculator: ")).lower()
    # Check if user wants to get out of calculator using 'exit' command
    if z=='exit':
        break
    #check if user input is as expected as defined in 'z'
    if z not in ('+', '-', '/', '*', 'sqrt'):
        print("Enter a valid operator to perform the calculation")
        continue
    if z == 'sqrt': #Square root operation - deals with single input
        y = float(input("Enter a number to find the square root: "))
        print("Square root of given number: ", y**0.5)
        continue
    # To perform rest of the operations - deals with two inputs
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    if z=='+': #Addition
        print("Sum of given numbers: ", a+b)
    elif z=='-': #Subraction
        print("Difference of given numbers: ", a-b)
    elif z=='/': #Division
        if b==0:
            print("Division by Zero Not Possible")
        else:
            print("Division - Quotient: ", a/b)
    elif z=='*': #Multiplication
        print("Product of given numbers: ", a*b)

