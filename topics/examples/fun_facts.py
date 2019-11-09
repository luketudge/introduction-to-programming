# -*- coding: utf-8 -*-
"""
A program to display some fun facts.
"""

# A function to help with the rest of the program:

def yorn(question):
    """Gets the user to answer a 'yes or no' question (YORN).

    The function is 'forgiving' and allows:
    * surrounding spaces
    * lower or uppercse answers
    * any word beginning with either 'y' or 'n'

    Returns a boolean, so that the function can be used in an 'if' statement.

    Example:
        >>> yorn('Would you like a buttered crumpet?')
        Would you like a buttered crumpet? (y/n) YES!
        True

    Arguments:
        question: A string prompt.
        The additional prompt '(y/n)' will be appended.

    Returns:
        Boolean
    """

    answer = ''

    while answer not in ['y', 'n']:
        answer = input(question + ' (y/n) ')
        answer = answer.strip().lower()[:1]

    if answer == 'y':
        return True
    else:
        return False


# The program itself:

fun_facts = ['a',
             'b',
             'c']

if yorn('Would you like to hear some fun facts?'):

    for fact in fun_facts:

        if yorn('Would you like me to SHOUT so you can hear clearly?'):
            fact = fact.upper()

        print('Ok, here you go:')
        print(fact)

        if not yorn('Would you like to hear another?'):
            break

print('Ok. Bye.')
