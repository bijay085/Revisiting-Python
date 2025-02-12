# on a string we can perform many opertion, but here we will do only basic 

# ----------1. conact : concatination means joining 2 string, not int just string.

str1 = "Hello"
str2 = "World"

print(str1 + str2)
print(str1 , str2) #this also return same , this is a kind of concat but not a conact. 


# ----------2. Length of a string, : counting alphabets

str3 = "Bijay"
count3 = len(str3)
print(count3) #5

#it counts spaces too

str4 = "Bi jay"
print(len(str4)) #6


# ----------3. indexing : postion number of each charcaters
#start with 0

str5 = "World Hello" #W=0, o =1, r=2....

print(str5[6]) #accessing according to index # H

index5 = str5[8] #accessing 8th index
print(index5) # l


print(str5[5]) #accessing according to index # space
print(str5[0]) #accessing according to index # W

# ----------4. Slicing, Important topic,, slicing means slicing from a character

str6 = "Game Of Throne"
print(str6)

sl6 = print(str6[2:7]) #starting:ending index , it print from 2 to 
sl6 = print(str6[2:9:2]) #starting:ending:position index 

#for easyness, by default it count last index even if we forgot to give last index and in starting 0

str7 = "College"
print(str7[:])



# ----------5. Negative Slicing 
str7 = "College"
print(str7[-6:-2])
print(str7[-2:-6]) #returns empty because, it starts from -2 to -6 which is inverse, 

#normally negative slicing is not that imp or used cuz it use same counting mechanism as normal slicing just indexing is in minus.
