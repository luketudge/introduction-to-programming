# -*- coding: utf-8 -*-
"""
Miscellaneous additional tools.
"""

import os


def remove_if_exists(filename):
    """Remove a file if it already exists.
    """
    
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass