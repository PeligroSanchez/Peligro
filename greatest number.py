first = int(input("Enter first number :"))
second = int(input("Enter second number :"))
third = int(input("Enter third number :"))
forth = int(input("Enter forth number :"))

if first < second and first < third and first < forth :
    print(first,"is the smallest number")
elif second < first and second < third and second < forth :
    print(second,"is the smallest number")
elif third < first and third < second and third < forth :
    print(third,"is the smallest number")
else:
    print(forth,"is the smallest number")

#Simple calculator program

# Function to add two numbers
num1 = 20
num2 = 12
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


print("Please select option"
      " -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")

# Take input from the user
select = int(input("Select options form 1, 2, 3, 4 :"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    print(num1, "+", num2, "=",
          add(num1, num2))

elif select == 2:
    print(num1, "-", num2, "=",
          subtract(num1, num2))

elif select == 3:
    print(num1, "*", num2, "=",
          multiply(num1, num2))

elif select == 4:
    print(num1, "/", num2, "=",
          divide(num1, num2))
else:
    print("Invalid input")
