# -*- coding: utf-8 -*-
"""
A program using the single function in the initials.py module.

* Get two users' full names.
* Generate abbreviated IDs for the users.
* Ensure these IDs are unique to each user.
"""

# Import statements should go at the top of a program.
# So others can see easily what additional modules are used.
import initials


name1 = input('User 1 enter your full name: ')
name2 = input('User 2 enter your full name: ')

# Try up to 3 letters from each name to get a unique abbreviated ID.
for n_letters in range(1, 4):
    ID1 = initials.get_initials(name1, n=n_letters)
    ID2 = initials.get_initials(name2, n=n_letters)

    # If the two IDs are not the same, we have tried enough letters.
    # So stop.
    if ID1 != ID2:
        break

# If the two IDs are still the same now, then even 3 letters wasn't enough.
# So append some numbers to make the IDs unique.
if ID1 == ID2:
    ID1 = ID1 + '1'
    ID2 = ID2 + '2'

result = "User 1 will be called '{}' and user 2 will be called '{}'."
print(result.format(ID1, ID2))
