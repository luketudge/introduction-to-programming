# -*- coding: utf-8 -*-
"""
Process html.
"""

import bs4
import regex


# %% Constants

PARSER = 'lxml'


# %% Regular expressions

# '.ipynb'
IPYNB_FILE_EXTENSION = regex.compile(r'(?<=\.)ipynb',
                                     flags=regex.V1)

# word character
# one or more word characters or '/'
# '/'
# one or more word characters
# '.html'
PATH_TO_HTML_FILE = regex.compile(r'^\w[\w\/]*\/(?=\w+\.html)',
                                  flags=regex.V1)


# %% Helper functions

def make_soup(html):
    """Convert html notebook to BeautifulSoup.
    """

    return bs4.BeautifulSoup(html, PARSER)


# %% Postprocessing

def replace_ipynb(soup, new='html'):
    """Change all links to ipynb files.
    """

    for link in soup.find_all(href=IPYNB_FILE_EXTENSION):
        link['href'] = IPYNB_FILE_EXTENSION.sub(new, link['href'])

    return soup


def flatten_links(soup):
    """Remove leading directories from paths to local html files.
    """

    for link in soup.find_all(href=PATH_TO_HTML_FILE):
        link['href'] = PATH_TO_HTML_FILE.sub('', link['href'])

    return soup
