#Arithmetic operators-perform simple calculations
num1 = 56
num2 = 8

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)

#Comparison operator-compare values
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)

#Assignment operator-assign values to variables
a = 200
print(a)

print(a + 20)

#Logic operators-and,or,not
x = 100
print(x < 250 and x > 1000)
print(x < 250 or x > 1000)

#Operator predence-order in which operations are executed
output = (100-4*3 / 1)
print(int(output))

#Write a simple python program that returns the area of a trapezium


# Function to calculate the area of a trapezium
def area_of_trapezium(a, b, h):
    return 0.5 * (a + b) * h

# Example values
a = 5.0  # length of the first parallel side
b = 7.0  # length of the second parallel side
h = 4.0  # height

# Calculate the area of the trapezium
area = area_of_trapezium(a, b, h)

# Output the result
print(f"The area of the trapezium with sides {a} and {b}, and height {h} is {area:.2f} square units.")

