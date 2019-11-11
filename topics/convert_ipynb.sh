#!/bin/bash

# Convert .ipynb to some more web-friendly formats.

# Markdown.
# Use these as the default pages linked from the README.
jupyter nbconvert --to markdown *.ipynb
sed -i "s/\.ipynb/.md/g" *.md

# HTML.
# Not really using these, but might as well make them.
# Put them in a separate folder to avoid cluttering the page.
jupyter nbconvert --to html *.ipynb --output-dir html
sed -i "s/\.ipynb/.html/g" html/*.html
