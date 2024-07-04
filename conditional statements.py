temperature = 46

if temperature < 25:
    print("It is cold")

elif temperature > 25:
    print("It is hot")

else:
    print("Normal temperature")

#Simple program of returning
first = 90
second = 45
third = 69

if first > second and first > third:
    print(first,"is the largest no.")
elif second > first and second > third:
    print(second,"is the largest no.")


    #Write a python program of showing if no. is even or odd

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example number
number = 25

# Check if the number is even or odd
result = check_even_odd(number)

# Output the result
print(f"The number {number} is {result}.")


