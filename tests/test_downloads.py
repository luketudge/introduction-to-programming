# -*- coding: utf-8 -*-

import os
import zipfile

import requests

from . import constants


# %% Helper Functions

def get_zip_contents(url):

    temp_filename = os.path.join(constants.BASE_PATH, 'temp.zip')

    try:
        os.remove(temp_filename)
    except FileNotFoundError:
        pass

    r = requests.get(url, params={'raw': 'true'})

    with open(temp_filename, mode='wb') as f:
        f.write(r.content)

    with zipfile.ZipFile(temp_filename) as f:
        contents = f.namelist()

    os.remove(temp_filename)

    return contents


# %% Test functions

def test_download_examples():

    contents = get_zip_contents(constants.REMOTE_URL_EXAMPLES)

    assert set(contents) == set(constants.EXAMPLE_FILES + constants.DATA_FILES)
