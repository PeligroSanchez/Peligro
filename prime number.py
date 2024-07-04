#Python program of checking whether it is a prime no. or not

num = 9

for i in range(2,num):
    if num % i ==0:
        print("Not Prime")
        break
else:
    print("Prime")
    

