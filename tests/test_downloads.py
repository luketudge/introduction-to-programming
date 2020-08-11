# -*- coding: utf-8 -*-

import os
import zipfile

import requests

from . import constants


# %% Helper functions

def delete_temp_file():

    try:
        os.remove(constants.TEMP_FILENAME)
    except FileNotFoundError:
        pass


def get_zip_contents(url):

    delete_temp_file()

    r = requests.get(url, params={'raw': 'true'})

    with open(constants.TEMP_FILENAME, mode='wb') as f:
        f.write(r.content)

    with zipfile.ZipFile(constants.TEMP_FILENAME) as f:
        contents = f.namelist()

    delete_temp_file()

    return contents


# %% Test functions

def test_download_examples():

    contents = get_zip_contents(constants.REMOTE_URL_EXAMPLES)

    assert set(contents) == set(constants.EXAMPLE_FILES + constants.DATA_FILES)
