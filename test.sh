#!/bin/bash

echo '#### Tests ####'
pytest --verbose tests

echo '#### Style checks ####'
flake8 content/examples
