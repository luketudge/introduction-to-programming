# -*- coding: utf-8 -*-
"""
* Ask the user to enter their name and surname.
* Find one interesting thing to say about their name:
  * If they are called 'David Hasselhoff',
  ask "Are you THE ..."
    * If they say yes,
    say "Wow!"
    * If they say no,
    say "Well that is quite a coincidence..."
  * Otherwise if their surname is 'Hasselhoff',
  ask "Any relation..."
    * If they say yes,
    say "Wow!"
    * If they say no,
    say "You never know..."
  * Otherwise if their initials are 'DH',
  say "You have the same initials..."
  * Otherwise if their first name is a variant of 'David',
  say "Well, your name is a bit like..."
  * Otherwise, as a last resort,
  say "Never mind, I suppose you could change it..."
"""

# Some preliminaries:

user_name = input('What is your name and surname? ')

# Perform a small bit of data cleaning:
# * strip away accidental surrounding spaces
# * convert the name to 'titlecase'
# (i.e. with initial capitals so it matches 'David Hasselhoff')
user_name = user_name.strip().title()

# Get the separate names and initials.
user_names = user_name.split()
user_firstname = user_names[0]
user_surname = user_names[1]
user_initials = user_firstname[0] + user_surname[0]


# Now the various conditions:

# Same exact name.
if user_name == 'David Hasselhoff':
    is_hoff = input('Are you THE David Hasselhoff? ')
    if is_hoff.strip().lower() == 'yes':
        print('Wow!')
    else:
        print('Well that is quite a coincidence that you have the same name.')

# Same first name.
elif user_surname == 'Hasselhoff':
    is_relation = input('Any relation to David Hasselhoff? ')
    if is_relation.strip().lower() == 'yes':
        print('Wow!')
    else:
        print('You never know, you might be.')

# Same initials.
elif user_initials == 'DH':
    print('You have the same initials as David Hasselhoff!')

# Similar first name.
elif user_firstname in ['Dave', 'Davy', 'Dafydd']:
    print("Your name is a bit like 'David', as in 'David Hasselhoff'.")

# Nothing interesting to say.
else:
    print("I suppose you could change your name to something more interesting, like 'David Hasselhoff'.")


# A final message:

print('I hope you enjoyed this exciting interactive program.')
