'''1. Write a program to find length of a string. '''

my_string = "helloworld"
print(len(my_string))
print(my_string)

'''2. Write a program to copy one string to another string.'''

string1 = "Organization"
string2 = string1
print("Original string is :",string1)
print("Copied String is :",string2)

'''3. Write a program to concatenate two strings.'''

string1 = "Zeeshan"
string2 = "Ramzan"
print(string1 +" "+ string2)

'''4. Write a program to compare two strings.'''
string1 = input("enter string 1")
string2 = input("enter string 2 :")
if string1 == string2:
    print("String1 is equal to string2")
else:
    print("strings are not equal")

'''5.Write a program to convert lowercase string to uppercase.'''
string1 = "zeeshan"
string2 = string1.upper()
print("Lower case string Is :",string1)
print("Converted into Uppercase :",string2)

'''6. Write a program to convert uppercase string to lowercase.'''
string1 = "ZEESHAN"
string2 = string1.lower()
print("Lower case string Is :",string1)
print("Converted into Lowercase :",string2)

''''7. Write a program to toggle case of each character of a string.'''
string1 = "Hello World"
string2 = string1.swapcase()
print("Original string:",string1)
print("Toggle string :",string2)

'''8. Write a program to find total number of alphabets, digits or special character in a string.'''
user = input("Enter your string")
alphabet = 0
digits = 0
special_char =0
for i in user:
    if i.isalpha():
        alphabet += 1
    elif i.isdigit():
        digits += 1
    else:
        special_char +=1
print("Alphabets is:",alphabet)
print("Digits is :" ,digits) 
print("Special Character is :" , special_char)                

'''9. Write a program to count total number of vowels and consonants in a string.'''
v = "aeiou"
vowels = 0
consonants = 0
user = input("enter string").lower()
for i in user:
 if i in v:
  vowels += 1 
 else:
        consonants += 1   
print("Vowels is : ",vowels)
print("Consonants is :",consinants)

'''10. Write a program to count total number of words in a string.'''
my_string = "malikzeeshan"
print(len(my_string))

'''11. Write a program to find reverse of a string.'''
string = "helloworld"   
print(string[::-1])

'''12. Write a program to check whether a string is palindrome or not.'''
string = input("enter a string :")
if string == string[::-1]:
    print(string , "is palindrome")
else:
    print(string,"is not palindrome")

'''13. Write a program to reverse order of words in a given string '''

input_string = input("Enter a string: ")
print("Reversed order of words:",input_string[::-1])

'''14. Write a program to find first occurrence of a character in a given string.'''
# Input a string and a character
input_string = input("Enter a string: ")
character = input("Enter a character: ")

index = input_string.find(character)

if index != -1:
    print("The first occurrence of character is at index:", index)
else:
    print("The character character is not found in the string.")


'''15. Write a program to find last occurrence of a character in a given string.'''

input_string = input("Enter a string: ")
character = input("Enter a character: ")

index = input_string.rfind(character)
if index != -1:
    print("The lasst occurrence of character is at index:", index)
else:
    print("The character character is not found in the string.")

'''16. Write a program to search all occurrences of a character in given string.'''
string = input("Enter a string: ")
char = input("Enter a character: ")
count = 0
for i in range(len(string)):
  if string[i] == char:
    count += 1
    print("The character", char, "is found at index", i) 

'''17. Write a program to count occurrences of a character in given string.'''
string = input("Enter a string: ")
char = input("Enter a character: ")
count = 0
for i in range(len(string)):
  if string[i] == char:
    count += 1
print("The character", char, "is found", count, "times")


'''18. Write a program to find highest frequency character in a string.'''
string = input("Enter a string: ")
char_count = {}
for char in string:
  if char in char_count:
    char_count[char] += 1
  else:
    char_count[char] = 1
max_count = 0
max_char = ""
for char, count in char_count.items():
  if count > max_count:
    max_count = count
    max_char = char

print("The highest frequency character is", max_char, "with count", max_count)

'''19. Write a program to find lowest frequency character in a string.'''
string = input("Enter a string: ")
char_count = {}
for char in string:
  if char in char_count:
    char_count[char] += 1
  else:
    char_count[char] = 1
min_count = float('inf')
min_char = ""
for char, count in char_count.items():
  if count < min_count:
    min_count = count
    min_char = char
print("The lowest frequency character is", min_char, "with count", min_count)    

'''20. Write a program to count frequency of each character in a string.'''

string = input("Enter a string: ")
char_count = {}
for char in string:
  if char in char_count:
    char_count[char] += 1
  else:
    char_count[char] = 1
print("Frequency of each character in the string:")
for char, count in char_count.items():
  print(char, ":", count)

''' 21. Write a program to remove first occurrence of a character from string.'''

string = input("Enter a string: ")
char = input("Enter a character to remove: ")
new_string = string.replace(char, "", 1)
print("The new string is:", new_string)

'''22. Write a program to remove last occurrence of a character from string.'''
string = input("Enter a string: ")
char = input("Enter a character to remove: ")
new_string = string.replace(char, "", 1)
print("The new string is:", new_string)


'''# 23. Write a program to remove all occurrences of a character from string.'''
string = input("Enter a string: ")
char = input("Enter a character to remove: ")

new_string = string.replace(char, "")
print("The new string is:", new_string)  

'''# 24. Write a program to remove all repeated characters from a given string.'''
string = input("Enter a string: ")
new_string = ""
for char in string:
  if char not in new_string:
    new_string += char
print("The new string is:", new_string)

'''25. Write a program to replace first occurrence of a character with another in a string.'''

string = input("Enter a string: ")
char = input("Enter a character to replace: ")
new_char = input("Enter a new character: ")
new_string = string.replace(char, new_char, 1)
print("The new string is:", new_string)

'''26. Write a program to replace last occurrence of a character with another in a string.'''
string = input("Enter a string: ")
char = input("Enter a character to replace: ")
new_char = input("Enter a new character: ")
new_string = string.replace(char, new_char, -1)
print("The new string is:", new_string)

'''# 27. Write a program to replace all occurrences of a character with another in a string.'''
string= input("Enter a string: ")
char = input("Enter a character to replace: ")
new_char = input("Enter a new character: ")
new_string = string.replace(char, new_char)
print("The new string is:", new_string) 


'''# 28. Write a program to find first occurrence of a word in a given string.'''
string = input("Enter a string: ")
word = input("Enter a word to find: ")
index = string.find(word)
if index != -1:
  print("The word is found at index", index)
else:
  print("The word is not found in the string")

'''# 29. Write a program to find last occurrence of a word in a given string.'''
string = input("Enter a string: ")
word = input("Enter a word to find: ")
index = string.rfind(word)
if index != -1:
  print("The word is found at index", index)
else:
  print("The word is not found in the string")

'''# 30. Write a program to search all occurrences of a word in given string.'''
string =input("Enter a string: ")
word = input("Enter a word to find: ")
index = string.find(word)
if index != -1:
  print("The word is found at index", index)
else:
  print("The word is not found in the string")

'''# 31. Write a program to count occurrences of a word in a given string.'''
string = input("Enter a string: ")
word = input("Enter a word to count: ")
count = string.count(word)
print("The word is found", count, "times")

'''# 32. Write a program to remove first occurrence of a word from string.'''
string = input("Enter a string: ")
word = input("Enter a word to remove: ")
new_string = string.replace(word, "", 1)
print("The new string is:", new_string)

'''# 33. Write a program to remove last occurrence of a word in given string.'''
string = input("Enter a string: ")
word = input("Enter a word to remove: ")
new_string = string.replace(word, "", 1)
print("The new string is:", new_string)

''' 34. Write a program to remove all occurrence of a word in given string.'''
string = input("Enter a string: ")
word = input("Enter a word to remove: ")
new_string = string.replace(word, "")
print("The new string is:", new_string)

''' 35. Write a program to trim leading white space characters from given string.'''
string = input("Enter a string: ")
new_string = string.lstrip()
print("The new string is:", new_string)

'''# 36. Write a program to trim trailing white space characters from given string.'''
string = input("Enter a string: ")
new_string = string.rstrip()
print("The new string is:", new_string)

'''# 37. Write a program to trim both leading and trailing white space characters from given string.'''
string = input("Enter a string: ")
new_string = string.strip()
print("The new string is:", new_string)

''' 38. Write a program to remove all extra blank spaces from given string.'''
string = input("Enter a string: ")
new_string = string.replace("  ", " ")
print("The new string is:", new_string)