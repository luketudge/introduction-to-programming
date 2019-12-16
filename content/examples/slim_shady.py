# -*- coding: utf-8 -*-
"""
The Slim Shady module.

A file to demonstrate the behavior of the __name__ special variable.
But in a hip way that young people can relate to.

Import this module elsewhere to see the value of __name__ for imported modules.
Run this module as a script to see the value of __name__ for a script.
"""

print('Hi!')

for reply in ['What?', 'Who?', __name__]:
    print('My __name__ is ...', reply)
