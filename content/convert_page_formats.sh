#!/bin/bash

# Convert the page files among various formats.
# The starting point is the jupyter notebooks.
# Turn these into markdown for the GitHub site.
# Turn markdown into html for offline viewing.


#### jupyter notebook to markdown ####

for FILENAME in *.ipynb; do

  NEWFILENAME="${FILENAME%.*}.md"

  # Convert with nbconvert, removing the hidden content.
  jupyter nbconvert --to=markdown --TagRemovePreprocessor.remove_cell_tags='{"remove-cell"}' --TagRemovePreprocessor.remove_all_outputs_tags='{"remove-output"}' $FILENAME

  # Replace links to notebooks with their markdown equivalents.
  sed --in-place "s/\.ipynb/.md/g" $NEWFILENAME

  # Remove non-printable escape sequences.
  sed --in-place "s/\[^m]*m//g" $NEWFILENAME

done


#### markdown to html ####

BASEDIRNAME=$(pwd)

# Get the GitHub markdown css,
# and change it so it applies to the whole document.
CSSFILENAME="$BASEDIRNAME/html/github-markdown.css"
wget -O $CSSFILENAME https://raw.githubusercontent.com/sindresorhus/github-markdown-css/gh-pages/github-markdown.css
sed --in-place "s/\.markdown-body/body/g" $CSSFILENAME

# pandoc can only find image and css files relative to the working directory,
# not relative to the location of the file that links to them,
# so we have to cd through the subdirectories containing markdown files.
for DIRNAME in . extras extras/software; do

  cd $DIRNAME

  for FILENAME in $(find -maxdepth 1 -name "*.md"); do

    # Skip READMEs other than the main one.
    if test "$DIRNAME" != "." -a "$FILENAME" = "./README.md"; then
      continue
    fi

    NEWFILENAME="${FILENAME%.*}.html"
    NEWFILENAME="${NEWFILENAME/\./$BASEDIRNAME/html}"

    # Convert with pandoc to self-contained html.
    pandoc --from=markdown --to=html --self-contained --css=$CSSFILENAME --mathml --output=$NEWFILENAME $FILENAME

    # Replace links to markdown files with their html equivalents.
    sed --in-place "s/\.md/.html/g" $NEWFILENAME

    # Repair links to files in other folders.
    sed --in-place "s/extras\///g" $NEWFILENAME
    sed --in-place "s/software\///g" $NEWFILENAME
    sed --in-place "s/examples\//..\/examples\//g" $NEWFILENAME

  done

  cd $BASEDIRNAME

done

# Convert the main README to an index.html.
mv html/README.html html/index.html
