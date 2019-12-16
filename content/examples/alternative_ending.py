# -*- coding: utf-8 -*-
"""
Tack an alternative ending onto a great work of literature.
"""

import os


# Jane Austen wrote in ASCII (though she didn't know it at the time),
# so we don't strictly need to specify UTF-8 as an encoding,
# but this is included in case we adapt the program to a non-ASCII text.
filename = 'austen-sense.txt'
encoding = 'utf-8'
filepath = os.path.join('data', filename)

alt_file_prefix = 'alternative_'
alt_filepath = os.path.join('data', alt_file_prefix + filename)
alt_ending = '\n\nBut then I woke up and it was all a dream.\n'

end_text = 'the end'

# strip() so that the end of the string is really the final characters,
# and does not include any trailing newlines.
text = open(filepath, encoding=encoding).read().strip()

# Remove any ending that might already be present in the file
# (as in the Austen file for example).
if text.lower().endswith(end_text):
    text = text[:-len(end_text)]

with open(alt_filepath, mode='w', encoding=encoding) as f:
    f.write(text + alt_ending)

# Check the end of the new file to test it has worked.
new_text = open(alt_filepath, encoding=encoding).read()
print(new_text[-500:])
