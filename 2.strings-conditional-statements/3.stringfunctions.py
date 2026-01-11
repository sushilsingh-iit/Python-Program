# Python treats strings as immutable objects, meaning you cannot modify them in place. Instead, Python provides a vast library of built-in string methods that return a new, modified copy of the string.

# Here is a breakdown of the most essential Python string functions, categorized by how they are used.
# 1. Changing Case

# These methods are useful for normalizing text (e.g., making user input case-insensitive).

#     lower(): Converts all characters to lowercase.

#     upper(): Converts all characters to uppercase.

#     title(): Capitalizes the first letter of every word.

#     capitalize(): Capitalizes only the very first letter of the string.

# Python

# text = "hello WORLD"

# print(text.lower())      # Output: "hello world"
# print(text.upper())      # Output: "HELLO WORLD"
# print(text.title())      # Output: "Hello World"
# print(text.capitalize()) # Output: "Hello world"

# 2. Cleaning and Editing

# These are crucial for data cleaning, such as removing extra whitespace or swapping words.

#     strip(): Removes leading and trailing whitespace (spaces, tabs, newlines). You can also pass a specific character to strip (e.g., .strip(',')).

#         Variations: lstrip() (left only) and rstrip() (right only).

#     replace(old, new): Replaces occurrences of a substring with a new one.

# Python

# raw_data = "   Python is fun!   "

# clean_data = raw_data.strip()
# print(clean_data)  # Output: "Python is fun!" (spaces gone)

# new_data = clean_data.replace("fun", "powerful")
# print(new_data)    # Output: "Python is powerful!"

# 3. Splitting and Joining

# These two functions are often used together to convert between Strings and Lists.

#     split(separator): Splits a string into a List, breaking it at the specified separator. If no separator is given, it splits by whitespace.

#     join(iterable): Joins a List of strings into a single String, using the string it is called on as the connector.

# Python

# csv_row = "Apple,Banana,Cherry"

# # String to List
# fruit_list = csv_row.split(",")
# print(fruit_list) # Output: ['Apple', 'Banana', 'Cherry']

# # List to String
# # Note: Syntax is "connector".join(list)
# new_string = " - ".join(fruit_list)
# print(new_string) # Output: "Apple - Banana - Cherry"

# 4. Searching and Counting

# Use these to find specific content within a string.

#     find(sub): Returns the index of the first occurrence of the substring. Returns -1 if not found.

#     count(sub): Returns the number of times a substring appears.

#     startswith(sub) / endswith(sub): Returns True or False.

# Python

# sentence = "The cat sat on the mat."

# print(sentence.find("cat"))      # Output: 4
# print(sentence.count("the"))     # Output: 1 (Case sensitive!)
# print(sentence.startswith("The"))# Output: True

# 5. Inspection (Is it...?)

# These methods return a Boolean (True or False) and are great for validating user input.
# Method	Checks if the string contains...
# isdigit()	Only numbers (0-9).
# isalpha()	Only letters (a-z).
# isalnum()	Alphanumeric characters (letters and numbers).
# isspace()	Only whitespace (spaces, tabs, newlines).
# isupper()	Only uppercase letters.

# Example:
# Python

# phone = "123456"
# print(phone.isdigit()) # Output: True

# username = "User123"
# print(username.isalpha()) # Output: False (contains numbers)

# Quick Summary Cheat Sheet
# Category	Top Functions
# Modify	.strip(), .replace(), .upper(), .lower()
# Structure	.split() (to list), .join() (to string)
# Search	.find(), .count(), .startswith()
# Check	.isdigit(), .isalpha()
# A Note on Formatting (f-strings)

# While not strictly a "function," f-strings (introduced in Python 3.6) are the modern standard for inserting variables into strings.
# Python

# name = "Alice"
# age = 30
# # The 'f' before the quotes allows you to put variables in {}
# print(f"{name} is {age} years old.")



str = "i am study python from apnacollege"
print (str.endswith("ege"))
str1 = "i am study python from apnacollege"
print (str1.capitalize())
str1 = str1.capitalize() # fro all time capitslize
print(str1)


str2 = "i am study python from apnacollege"
print (str2.replace("python " , "c++"))

str3 = "i am study python from apnacollege"
print(str3.find("python")) # if not found print -1 

str4 = "i am study python from apnacollege"
print(str4.count("am")) # count the occurrence of substring 