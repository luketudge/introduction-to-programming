#!/bin/bash

jupyter-book build content/
ghp-import -n -p -f content/_build/html
