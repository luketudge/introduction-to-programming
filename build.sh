#!/bin/bash

cd content/examples
rm intro_prog_examples.zip
zip intro_prog_examples.zip *.* data/*.*
cd ../..
jupyter-book clean content/
export PYTHONPATH="$PWD"
jupyter-book build content/ -n
