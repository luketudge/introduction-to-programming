# -*- coding: utf-8 -*-
"""
A program to display some fun facts.
"""

# A function to help with the rest of the program:

def yorn(question):
    """Gets the user to answer a 'yes or no' question (YORN).

    The function is 'forgiving' and allows:
    * surrounding spaces
    * lower or uppercase answers

    Returns a boolean, so that the function can be used in an 'if' statement.

    Example:
        >>> yorn('Would you like a buttered crumpet?')
        Would you like a buttered crumpet? (y/n)     Y
        True

    Arguments:
        question: A string prompt.
        The additional prompt ' (y/n) ' will be appended.

    Returns:
        Boolean
    """

    answer = ''

    while answer not in ['y', 'n']:
        answer = input(question + ' (y/n) ')
        answer = answer.strip().lower()

    if answer == 'y':
        return True
    else:
        return False


# The program itself:

fun_facts = ['Elephants gestate for 21 months.',
             'There are more tin cans than people.',
             'The record number of marshmallows stuffed up one nostril is 604.']

if yorn('Would you like to hear some fun facts?'):

    for fact in fun_facts:

        if yorn('Would you like me to SHOUT so you can hear clearly?'):
            fact = fact.upper()

        print('Ok, here you go:')
        print(fact)

        if not yorn('Would you like to hear another?'):
            break

print('Ok. Bye.')
