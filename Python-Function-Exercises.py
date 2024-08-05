# Student name:  Makhubela HP
# Student no: 218084338
# Date: August/05/2024
# Assignment 3: Python

print("Problem 1")
print()
s = 'fullstackslp'
# 'f'
print(s[0])
# 'p'
print(s[-1])
# 'stack'
print(s[4:9])
# 'slp'
print(s[-3:])
# 'cks'
print(s[5:8])
# Bonus: Use indexing to reverse the string
print(s[::-1])
print()
print("Problem 2 - LISTS")
print()
# Given dictionaries
d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

# Grabbing 'hello' using indexing
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

print()
print("Problem 4 - SETS")
print()
# Finding unique values using a set
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
unique_values = set(mylist)
print(unique_values)

print()
print("Problem 5 - FORMATTING")
print()

# Given variables
age = 45
name = "Kyle"

# Using .format() for string formatting
print("Hello, my dog's name is {x} and he looks {y} years old".format(x=name, y=age))
