#!/bin/bash

# Convert .ipynb to markdown.
# Use the markdown pages as the default pages linked from the README.

jupyter nbconvert --to=markdown --TagRemovePreprocessor.remove_cell_tags='{"remove-cell"}' *.ipynb
sed -i "s/\.ipynb/.md/g" *.md
