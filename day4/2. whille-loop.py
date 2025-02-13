#testing my iq in while loop 

str1 = "Python"
#Now we want to print it 5 times but in another way

# """ is used for multiline comment but this not showing in color as # 
"""
while (len(str1) >= 0):
    print("str1")
    len(str1) -= 1
"""
 #wrong above cuz we cannot directly update or change value of len(str1) else we can store and use as another variable 

count = len(str1) #store

while count > 0:
    print(f"{count} Python")
    count -= 1

print(count) #0

#infinite while , we use in like password login, like while password is wrong enter again.

while True:
    print("Me") #now it will go infinite times, we need to stop
    #True = False #wrong not assignable
    #return False #wrong not a function
    break #correct to come out of loop even condition satisfying

#using while to print from list '

mylist = [1,3,5,6,7,8]
print(mylist[0])  
print(mylist[1])  
print(mylist[2])  
print(mylist[3]) #we can go like this but we can createa logic from this simple code  

print("Now using while loop ")

i = 0 
while i < len(mylist):
    print(mylist[i])
    i += 1 #cannot use i++ cuz python dont support
    