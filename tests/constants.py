# -*- coding: utf-8 -*-

import os


# %% Paths & URLs

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

TEMP_FILENAME = os.path.join(BASE_PATH, 'temp.zip')

LOCAL_URL = 'file://' + os.path.join(os.path.dirname(BASE_PATH), 'content', 'html')

REMOTE_URL = 'https://github.com/luketudge/introduction-to-programming/blob/{}/'

TOPICS_PAGE = 'content/index.md'

BRANCHES = ['master', 'in-progress']


# %% Versions

TOPICS_VERSIONS = ([REMOTE_URL.format(b) + TOPICS_PAGE for b in BRANCHES] +
                   [os.path.join(LOCAL_URL, 'index.html')])

VERSION_IDS = BRANCHES + ['local']


# %% Pages

TOPIC_PAGES = [
    'Creating a computer program with Python',
    'Variables and data types',
    'Sequences and mappings',
    'Conditions',
    'Iteration',
    'Functions',
    'Modules',
    'The standard library',
    'Files',
    'The command line',
    'Testing',
    'GitHub',
    'Array computing',
    'Images',
    'Data analysis',
    'The Internet',
]


# %% Filenames

EXAMPLE_FILES = [
    'age_next_year.py',
    'alternative_ending.py',
    'circle.py',
    'coordinates.py',
    'fun_facts.py',
    'greeting.py',
    'greeting_personal.py',
    'guardian_top_article.py',
    'guess_the_animal.py',
    'hoff.py',
    'horses.py',
    'html_examples.html',
    'ids.py',
    'initials.py',
    'make_monthly_directories.py',
    'my_program.py',
    'name_trivia.py',
    'slim_shady.py',
    'spoonerisms.py',
    'test_math_is_working_as_normal.py',
    'test_spoonerisms.py',
]

DATA_FILES = [
    'austen-sense.txt',
    'guardian_taramasalata.json',
    'hamburger_emoji.png',
    'kentucky_derby.csv',
    'melville-moby_dick.txt',
    'penguins.csv',
    'penguins.html',
    'penguins.svg',
    'penguins_DE.csv',
    'README.md',
    'street_scene.jpg',
    'top_10_bands.txt',
    'top_5_bands_LATIN1.txt',
    'top_5_bands_UTF8.txt',
]

DATA_FILES = ['data/' + f for f in DATA_FILES]
