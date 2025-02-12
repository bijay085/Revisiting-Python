# 8. Extract `"John"` from the string `"Mr. John Wick"` without directly typing `"John"`.  

str1 = "Mr. John Wick"

#split method 
word = str1.split()
print(word[1])

#find method and slicing
ind = str1.find("John")
print(ind)

print(str1[ind:ind+4])