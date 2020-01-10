#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run all the build steps.
"""

import glob
import os

from tools import conversions
from tools import zipfiles


# %% Paths

base_path = os.path.dirname(os.path.abspath(__file__))

content_path = os.path.join(base_path, 'content')

print('building from', content_path)

html_path = os.path.join(content_path, 'html')
examples_path = os.path.join(content_path, 'examples')


# %% Conversion to markdown

ipynb_filenames = glob.glob(os.path.join(content_path, '*.ipynb'))

for filename in ipynb_filenames:
    conversions.ipynb_to_markdown(filename)
    print('converted', filename)


# %% zip file of example programs

# Covers all standard files but excludes hidden, __pycache__, etc.
files_pattern = '*.*'

# Covers both .py and .ipynb.
python_pattern = '*.*py*'

examples_patterns = [
    python_pattern,
    os.path.join('data', files_pattern),
]

destination = os.path.join(examples_path, 'intro_prog_examples.zip')

zipfiles.zip_all(destination,
                 path=examples_path,
                 patterns=examples_patterns)

print('zipped', destination)
