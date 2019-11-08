# -*- coding: utf-8 -*-
"""
A program providing a single function for getting the intials from a name.
"""

def get_initials(name, n=1, uppercase=False):
    """Gets the initials from a name.

    Example:
        >>> get_initials('Mildred Bonk')
        'mb'

    Arguments:
        name: A string containing exactly two names.
        n: The number of characters from each name to include in the initials.
        uppercase: Whether to make the initials UPPERCASE.

    Returns:
        A string containing the initials.

    Raises:
        ValueError: name did not contain exactly two names.
    """

    names = name.split()
    n_names = len(names)

    if n_names != 2:
        error_message = "'{}' contains {} names but should contain 2."
        raise ValueError(error_message.format(name, n_names))

    firstname = names[0]
    surname = names[1]
    initials = firstname[:n] + surname[:n]

    if uppercase:
        return initials.upper()
    else:
        return initials.lower()


# Test the function.
if __name__ == '__main__':

    # With default behavior.
    print(get_initials('Mildred Bonk'))

    # Using the keyword arguments.
    print(get_initials('Mildred Bonk', n=2, uppercase=True))
