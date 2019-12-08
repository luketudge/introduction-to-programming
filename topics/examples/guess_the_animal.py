# -*- coding: utf-8 -*-
"""
Play a game of 'guess the animal', with hints.
"""

correct_answer = 'african swallow'

hints = ['weighs five ounces',
         'beats its wings 43 times per second',
         'is not migratory',
         'has dorsal guiding feathers',
         'can carry a coconut',
         'is not European']

print("I'm thinking of an animal.")


for h in hints:

    # Get the guess and 'clean' it.
    print('Hint: It {}.'.format(h))
    guess = input("What is it (or type 'q' to quit)? ")
    guess = guess.strip().lower()

    # If the guess is empty, keep asking.
    while guess == '':
        guess = input("Enter the name of an animal (or 'q' to quit): ")
        guess = guess.strip().lower()

    # Deal with the 'quit' option first.
    if guess == 'q':
        print('So you give up, eh?')
        break

    # Check the guess and stop if correct.
    if guess == correct_answer:
        print('Correct!')
        break
    else:
        print("No, that's not it.")


# A final message revealing (or confirming) the answer.
print('It was the {}.'.format(correct_answer))
