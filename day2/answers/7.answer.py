# 7. Take a **full name input** from a user and print:  
#    - Only the **first name**.  
#    - Only the **last name**.  
#    - The full name in **uppercase**.  

name = input("Enter your full name:")

splitName = name.split() #inside bracket we use a indexing suppose, space, command, " ", / etc 

print(splitName[0])
print(splitName[1])

#uppercase 
print(name.upper())
print(name.capitalize())