#!/bin/bash

# Convert .ipynb to some more web-friendly formats.

# Markdown.
# Use these as the default pages linked from the README.
jupyter nbconvert --to markdown *.ipynb
sed -i "s/\.ipynb/.md/g" *.md
