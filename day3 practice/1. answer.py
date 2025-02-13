# 1. Take a string input from the user and print its **length**, **first character**, and **last character**.  

stringInput = input("Enter a string: ")

#legth of the string
length1 = len(stringInput)
print(f"Length of string {stringInput} is {length1}")

#first character of the string
print(f"First character of string {stringInput} is {stringInput[0]}")

#last character of the string
print(f"Last character of string {stringInput} is {stringInput[length1-1]}")