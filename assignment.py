#Python program that prompts a user to enter a letter and checks whether it is a component or a vowel

a = input("Enter the alphabet :")

if a in ('a','e','i','o','u','A','E','I','O','U'):
    print(a,"is a vowel")

else:
    print(a,"is a consonant")

