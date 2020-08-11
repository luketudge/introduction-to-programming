# -*- coding: utf-8 -*-
"""
Process html.
"""

import base64
import os

import bs4
import regex


# %% Regular expressions

# '.ipynb'
IPYNB_FILE_EXTENSION = regex.compile(r'(?<=\.)ipynb',
                                     flags=regex.V1)

# word character
# one or more word characters or '/'
# '/'
# one or more word characters (file name)
# '.'
# one or more word characters (file format)
PATH_TO_IMAGE = regex.compile(r'^\w[\w\/]*\/(?P<filename>\w+\.(?P<format>\w+))',
                              flags=regex.V1)


# %% Helper functions

def make_soup(html):
    """Convert html notebook to BeautifulSoup.
    """

    return bs4.BeautifulSoup(html)


# %% Postprocessing

def replace_ipynb(soup, new='html'):
    """Change all links to ipynb files.
    """

    for link in soup.find_all(href=IPYNB_FILE_EXTENSION):
        link['href'] = IPYNB_FILE_EXTENSION.sub(new, link['href'])

    return soup


def embed_images(soup, paths=['.']):
    """Embed linked images.

    Arguments:
        soup: bs4.BeautifulSoup of html
        paths: iterable of paths on which to search for image files
    """

    for link in soup.find_all('img', src=PATH_TO_IMAGE):

        match = PATH_TO_IMAGE.search(link['src'])
        filename = match.group('filename')
        fileformat = match.group('format')

        for p in paths:
            try:
                data = open(os.path.join(p, filename), mode='rb').read()
            except FileNotFoundError:
                pass

        embedded_image = base64.b64encode(data).decode()

        link['src'] = 'data:image/{};base64,{}'.format(fileformat, embedded_image)

    return soup
