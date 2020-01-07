#!/bin/bash

if test -z "$VIRTUAL_ENV"; then
    echo "No virtual environment detected. Exiting."
    exit 1
fi

pip install -r requirements.txt
jupyter contrib nbextension install --user
