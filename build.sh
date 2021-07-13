#!/bin/bash

cd content/examples
rm intro_prog_examples.zip
zip intro_prog_examples.zip *.* data/*.*
cd ../..
jupyter-book clean content/
jupyter-book build content/ -n -vvv
