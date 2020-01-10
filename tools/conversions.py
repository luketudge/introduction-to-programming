# -*- coding: utf-8 -*-
"""
Convert IPython notebooks to other formats.
"""

import nbconvert
import nbformat
import regex


# %% Constants

NOTEBOOK_VERSION = 4
OUTPUT_ENCODING = 'utf-8'


# %% Regular expressions

ANSI_ESCAPE = regex.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])',
                            flags=regex.V1)

# Uncompiled because {} will be replaced with different patterns.
CODE_BLOCK = r'(?<=```)python(?=\n.*{}.*\n```)'

IPYNB_FILE_LINK = regex.compile(r'(?<=\w\.)ipynb(?=[#\)])',
                                flags=regex.V1)


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


# %% Postprocess

def remove_ansi(text):
    """Remove ANSI escape sequences from a string.
    """
    
    return ANSI_ESCAPE.sub('', text)


def replace_ipynb(markdown, new='md'):
    """Change all links to ipynb files in markdown.
    """
    
    return IPYNB_FILE_LINK.sub(new, markdown)


def change_syntax_highlight(markdown, new='', pattern='^(!|%)'):
    """Change the syntax highlight header of given code blocks in markdown.
    
    Arguments:
        markdown: string of markdown
        new: replacement style
        pattern: change only code blocks that contain this regular expression
    """
    
    block_pattern = CODE_BLOCK.format(pattern)
    block_pattern = regex.compile(block_pattern,
                                  flags=regex.V1 | regex.MULTILINE)

    return block_pattern.sub(new, markdown, )


# %% Write

def write(content, filename):
    """Write text content to file.
    """
    
    with open(filename, mode='w', encoding=OUTPUT_ENCODING) as f:
        f.write(content)


# %% Full 'pipelines'

def ipynb_to_markdown(filename_in, filename_out=None):
    """Convert ipynb file to markdown file.
    """
    
    if filename_out is None:
        filename_out = filename_in.rsplit('.', 1)[0] + '.md'
    
    notebook = read(filename_in)
    
    remove_cells(notebook)
    remove_output(notebook)
    
    md = convert(notebook, 'md')
    md = replace_ipynb(md)
    md = remove_ansi(md)
    md = change_syntax_highlight(md)
    
    write(md, filename_out)
