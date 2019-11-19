# -*- coding: utf-8 -*-
"""
Create multiple directories.

The directories are named by year, with subdirectories for each month.
We could use these directories for organizing invoices, for example.
"""

# The os module from the standard library.
# This module provides functions for creating directories.
import os


main_dirname = 'invoices'

years = range(2015, 2020)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for y in years:
    for m in months:
        new_dirname = os.path.join(main_dirname, str(y), m)
        os.makedirs(new_dirname)
        print('created', new_dirname)
