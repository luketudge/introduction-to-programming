# -*- coding: utf-8 -*-
"""
A module for working with circles.
"""

import math


def area(radius):
    """Calculates the area of a circle from its radius.

    Example:
        >>> area(51)
        8171.28

    Returns: float
    """

    return math.pi * radius**2


def circumference(radius):
    """Calculates the circumference of a circle from its radius.

    Example:
        >>> circumference(51)
        320.44

    Returns: float
    """

    return 2 * math.pi * radius


# Tests.
if __name__ == '__main__':

    print(area(51))
    print(circumference(51))
