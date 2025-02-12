str1 = "I am a Student of my class."

# -----------1. endswith  : endswith("value") : return true if there is , else false

print(str1.endswith("nt")) #false
print(str1.endswith("ss")) #false
print(str1.endswith("ss.")) #true

print("College".endswith("ege")) #true

# -----------2. capitalize : only 1st character, and makes all small even if it is capital

str2 = "college STUDENT"

print(str2.capitalize()) #College student

print("baBy".capitalize()) #Baby

print(str2) #college STUDENT -> no changes in old string

# -----------3. Replace : replace(old,new)

str3 = "Baby Coder"

print(str3.replace("Coder","Bolder"))
print(str3) #Baby COder -> No changes in old string


print(str3.replace("er","FO"))

str4 = "Games fames Name"
print(str4.replace("ames", "")) #G f Name


# -----------4. find
str5 = "Loren Bhai sab Random Words For this paragraph No needed much thing with the wallet of the thief of the game"

print(str5.find("wallet")) #return indexing

str6 = "College Is mine college ok My College"
print(str6.find("college")) # 0  (First "College" at index 0)

print("Laptop".find("p"))

# -----------5. count 

str7 = "Mobile"
print(str7.count("o"))

str7 = "Voice Of Voice Gone"
print(str7.count("o"))

str7 = "This will be a test Test test paragraph a test paragraphs"
print(str7.count("test")) # 3 test 
print(str7.count("a")) # 8 a 