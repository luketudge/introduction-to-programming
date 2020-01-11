# -*- coding: utf-8 -*-
"""
Process markdown.
"""

import regex


# %% Regular expressions

ANSI_ESCAPE = regex.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])',
                            flags=regex.V1)

# '```python'
# newline
# zero or more characters
# {pattern}
# zero or more characters
# newline
# '```'
# (Uncompiled because {pattern} will be replaced.)
CODE_BLOCK = r'(?<=```)python(?=\n.*{}.*\n```)'

# one or more word characters
# '.ipynb'
# '#' or ')' (possible endings for link refs in markdown)
IPYNB_FILE_LINK = regex.compile(r'(?<=\w\.)ipynb(?=[#\)])',
                                flags=regex.V1)


# %% Postprocessing

def remove_ansi(text):
    """Remove ANSI escape sequences from a string.
    """

    return ANSI_ESCAPE.sub('', text)


def replace_ipynb(markdown, new='md'):
    """Change all links to ipynb files.
    """

    return IPYNB_FILE_LINK.sub(new, markdown)


def replace_syntax_highlight(markdown, new='', pattern='^(!|%)'):
    """Change the syntax highlight header of given code blocks.

    Arguments:
        markdown: string of markdown
        new: replacement style
        pattern: change only code blocks that contain this regular expression
    """

    block_pattern = CODE_BLOCK.format(pattern)
    block_pattern = regex.compile(block_pattern,
                                  flags=regex.V1 | regex.MULTILINE)

    return block_pattern.sub(new, markdown)
