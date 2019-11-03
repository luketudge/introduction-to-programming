#!/bin/bash

# Convert .ipynb to some more web-friendly formats.
for FORMAT in markdown html
do
  jupyter nbconvert --to $FORMAT *.ipynb
done

# In the generated files, replace .ipynb with the extension of each format.
# So links to other topic pages will link to the version with the same format.
for SUFFIX in md html
do
  sed -i "s/\.ipynb/.$SUFFIX/g" *.$SUFFIX
done
