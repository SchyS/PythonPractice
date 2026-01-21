def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

selection = int(input("Choose Your Operation: \n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nChoice: "))

n1 = int(input("Enter Your First Number: "))
n2 = int(input("Enter Your Second Number: "))

def calculation(selection, n1, n2):
    if selection == 1:
        return add(n1, n2)
    elif selection == 2:
        return subtract(n1, n2)
    elif selection == 3:
        return multiply(n1, n2)
    elif selection == 4:
        return divide(n1, n2)
    else:
        print("The selction you have made does not exist. Please try again.")
    
print(calculation(selection, n1, n2))