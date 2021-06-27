# -*- coding: utf-8 -*-

import os


# %% Paths & URLs

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

LOCAL_URL = 'file://' + os.path.join(os.path.dirname(BASE_PATH), 'content', '_build', 'html', 'index.html')
REMOTE_URL = 'https://luketudge.github.io/introduction-to-programming/'
REMOTE_URL_EXAMPLES = 'https://github.com/luketudge/introduction-to-programming/blob/master/content/examples/intro_prog_examples.zip'


# %% Pages

TOPIC_PAGES = [
    'Welcome',
    'Setup',
    'Readings',
    'Glossary',
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
    'Natural language processing',
    'The internet',
    'Relational databases',
]


# %% Filenames

EXAMPLE_FILES = [
    'README.md',
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
    'pedantry.py',
    'penguins.html',
    'slim_shady.py',
    'songs_tables.sql',
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
    'penguins.svg',
    'penguins_DE.csv',
    'penguins.xlsx',
    'README.md',
    'songs.csv',
    'songs.db',
    'songs.xlsx',
    'street_scene.jpg',
    'top_10_bands.txt',
    'top_5_bands_LATIN1.txt',
    'top_5_bands_UTF8.txt',
]

DATA_FILES = ['data/' + f for f in DATA_FILES]
