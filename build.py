# -*- coding: utf-8 -*-
"""
Run all the build steps.
"""

import glob
import os

from tools import convert
from tools import misc


# %% Paths

base_path = os.path.dirname(os.path.abspath(__file__))

content_path = os.path.join(base_path, 'content')
examples_path = os.path.join(content_path, 'examples')

image_paths = [
    os.path.join(content_path, 'images'),
    os.path.join(examples_path, 'data'),
]

print('building from', content_path)


# %% glob patterns

# Covers all standard files but excludes hidden, __pycache__, etc.
files_pattern = '*.*'

# Covers both .py and .ipynb.
python_pattern = '*.*py*'

html_pattern = '*.html'
sql_pattern = '*.sql'

examples_patterns = [
    python_pattern,
    html_pattern,
    sql_pattern,
    os.path.join('data', files_pattern),
]


# %% Find files

ipynb_filenames = glob.glob(os.path.join(content_path, '*.ipynb'))


# %% Convert ipynb files

for filename in ipynb_filenames:
    
    print('ipynb -> html', filename)

    filename_out = misc.strip_extension(os.path.basename(filename)) + '.html'
    filename_out = os.path.join(content_path, filename_out)

    convert.ipynb_to_html(filename, filename_out, image_paths=image_paths)


# %% Create zip file of example programs

destination = os.path.join(examples_path, 'intro_prog_examples.zip')

misc.zip_all(destination,
             path=examples_path,
             patterns=examples_patterns)

print('zipped', destination)
