# -*- coding: utf-8 -*-
"""
A program to tell the user some facts about their name.
The program uses various string methods.
"""

# Get the user's full name.
# For neatness, strip any surrounding spaces.
name = input('What is your full name (name and surname)? ')
name = name.strip()

# SHOUT their name.
shouty_name = name.upper()
msg = 'This is what your name sounds like shouted out loud: {}!'
print(msg.format(shouty_name))

# Count occurrences of the letter 'i'.
letter = 'i'
letter_count = name.lower().count(letter)
msg = "The letter '{}' occurs {} times in your name."
print(msg.format(letter, letter_count))

# Imitate Sean Connery.
connery_name = name.replace('s', 'sh').replace('S', 'Sh')
msg = "Sean Connery pronounces your name as '{}'."
print(msg.format(connery_name))
