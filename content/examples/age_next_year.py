# -*- coding: utf-8 -*-
"""
A program to get the user's age and tell them how old they will be in one year.
"""

# Get the user's input and convert it to integer type.
age = input('How old are you? ')
age = int(age)

# Calculate their age in one year using some advanced math.
age_next_year = age + 1

# Print out a message together with the result.
message = 'In one year you will be: ' + str(age_next_year)
print(message)
