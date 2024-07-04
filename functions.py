y = min(23, 56, 1000, 5647)
print(y)

x = max(90, 2, 76, 14)
print("The maximum number is", x)

z = pow(2 , 3)
print(z)

#User-defined functions
def school():
    print("eMobilis")
school() #This is calling a function

def multiply():
    num1 = 5
    num2 = 6
    print(num1 * num2)
multiply()

#Parameters and arguments-function to add two numbers
def add(a, b):
    print(a + b)
add(5, 6)
add(10, 15)
add(25, 30)
add(45, 25)

def employee(fullname,age,salary,phonenumber,position):
    print(fullname,age,salary,phonenumber,position)

employee("Job Kamau",45,500000,716363753,"CEO")
employee("Jane Kirui", 51,30000,71542931,"Secretary")
employee("Mark Mugo",34,16000,72834127,"Clerk")
employee("Elsa Wanjiru",40,200000,74872138,"Managing Director")