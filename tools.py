"""
Misc tools for building the book.
"""

import nbformat


HEADER_TEXT = """
# example program

You can download all the example programs [here](https://github.com/luketudge/introduction-to-programming/blob/master/content/examples/intro_prog_examples.zip?raw=true).
"""


def code_to_node(source):
    """Converts a string of code to nbformat.NotebookNode.
    """

    nb = nbformat.v4.new_notebook()
    title_cell = nbformat.v4.new_markdown_cell(HEADER_TEXT)
    code_cell = nbformat.v4.new_code_cell(source)
    nb['cells'].extend([title_cell, code_cell])

    return nb
