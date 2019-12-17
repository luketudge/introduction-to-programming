#!/bin/bash

echo '#### Tests ####'
pytest -v tests

echo '#### Style checks ####'
flake8 content
