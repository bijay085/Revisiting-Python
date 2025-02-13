
# we use break to break obv, means suppose in a loop condition is satisfied entered into the loop found break means stop the loop after break word not even1 line more.

n = 6
# if n < 10:  # we cannot use break in conditional statment, break is used in loop only

while n < 10:
    print(n)
    n += 1
    break

#lets see in for loop with else statment 
for i in range(0, 100, 5):
    print(i)
    
    if i == 25:
        print("25 found")
        break  # Loop stops here, so "Statement after break keyword" will never print
    
    print("25 not found")  # This still runs for all values except 25

else:
    print("Loop worked fully successfully, won't print if loop breaks")

print("Everything ended, and this is the final statement. It will print even if the loop is broken.")


#simple break logic statment
for i in range(1, 10):
    if i == 5:
        break  # Stops the loop when i is 5
    print(i)


# continue 
for i in range(1, 10):
    if i == 5:
        continue  #Skips 5, but continues the loop
    print(i)

