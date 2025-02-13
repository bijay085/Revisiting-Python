# list of name

names = ["Bijay", "Kaushal", "Bibek", "Game", "Over", "F1 F2", "Over"]

for value in names:
    #print(names) #print full list till the value goes
    print(value)

#now in tuple
print("\nIn tuple")
games = ("g1", "g2", "g3", "g4", "g4", "g5")

for value in games:
    print(value)
print("\n")

# in string and | using for and else  | success
str1 = "Missicialepleous" #not a word

for val in str1:
    print(val)
#to make sure loop run completely safely then we can use 'else' yes it is unique thing
else: 
    print("Loop ran successfullly")
    
# in string and using | for and else | not success
str2 = "break" #not a word

for val in str2:
    print(val)
    break
#to make sure loop run completely safely then we can use 'else' yes it is unique thing
else: 
    print("Loop ran successfullly")
#this wont get executed cuz loop not run fully safely there is break in python
