# range is nothing but a function used as in loop

# suppose range of 5

for i in range(5):
    print(i) 
print("\n")

for i in range(0,7):
    print(i)
print("\n")

for i in range(0,9,2):
    print(i)
print("\n")

#we use range in for loop mostly

#working in list
fruits = ["Apple", "Banana", "Cherry"]

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
