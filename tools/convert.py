# -*- coding: utf-8 -*-
"""
Convert IPython notebooks to other formats.
"""

import nbconvert
import nbformat

from . import html
from . import markdown
from . import misc


# %% Constants

NOTEBOOK_VERSION = 4
OUTPUT_ENCODING = 'utf-8'


# %% Exporters

md_exporter = nbconvert.MarkdownExporter()
html_exporter = nbconvert.HTMLExporter()

exporters = {
    'md': md_exporter,
    'html': html_exporter,
}


# %% Read

def read(filename):
    """Read a notebook from file.
    """

    return nbformat.read(filename, as_version=NOTEBOOK_VERSION)


# %% Preprocess

def has_tag(cell, tag):
    """Check if a notebook cell has a given tag.
    """

    tags = cell['metadata'].get('tags', list())

    return tag in tags


def remove_cells(notebook, tag='remove-cell'):
    """Remove all cells with a given tag.
    """

    notebook.cells = [cell for cell in notebook.cells if not has_tag(cell, tag)]


def remove_output(notebook, tag='remove-output'):
    """Remove output from all cells with a given tag.
    """

    for cell in notebook.cells:
        if has_tag(cell, tag) and 'outputs' in cell:
            cell['outputs'] = []


# %% Convert

def convert(notebook, to):
    """Convert notebook to another format.
    """

    return exporters[to].from_notebook_node(notebook)[0]


# %% Write

def write(content, filename):
    """Write text content to file.
    """

    with open(filename, mode='w', encoding=OUTPUT_ENCODING) as f:
        f.write(content)


# %% Pipelines

def ipynb_to_markdown(filename_in, filename_out=None):
    """Convert ipynb file to markdown file.
    """

    if filename_out is None:
        filename_out = misc.strip_extension(filename_in) + '.md'

    notebook = read(filename_in)

    remove_cells(notebook)
    remove_output(notebook)

    content = convert(notebook, 'md')
    content = markdown.replace_ipynb(content)
    content = markdown.remove_ansi(content)
    content = markdown.replace_syntax_highlight(content)

    write(content, filename_out)


def ipynb_to_html(filename_in, filename_out=None):
    """Convert ipynb file to html file.
    """

    if filename_out is None:
        filename_out = misc.strip_extension(filename_in) + '.html'

    notebook = read(filename_in)

    remove_cells(notebook)
    remove_output(notebook)

    content = convert(notebook, 'html')
    content = html.make_soup(content)
    content = html.replace_ipynb(content)
    content = html.flatten_links(content)

    write(str(content), filename_out)
