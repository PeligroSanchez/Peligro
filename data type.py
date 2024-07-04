#Data type

number = 78 #int
num = 45.09 #float
greeting = "How are you doing" #str
Is_Programming_Interesting = True #bool
devices = ["laptop","computer","tablet","phone"] #list
browser = ("opera","firefox","safari","brave") #tuple
countries = {"Kenya","Uganda","Tanzania"} #set
employee ={
    "firstname" : "Jane",
    "age" : 29,
    "Nationality" : "Kenyan",
    "emailaddress" : "jane@gmail.com"
} #Dictionery

print(Is_Programming_Interesting)
print(num)
print(countries)
print(employee["firstname"])

#Determining data type
print(type(countries))
print(type(employee))

#Type casting-It is the process of converting one data type to another
print(int(num))
print(float(number))

