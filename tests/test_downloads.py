# -*- coding: utf-8 -*-

import os
import zipfile

import pytest
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

@pytest.mark.parametrize('branch', constants.BRANCHES)
def test_download_examples(branch):

    url = constants.REMOTE_URL.format(branch) + 'content/examples/intro_prog_examples.zip'
    contents = get_zip_contents(url)

    assert set(contents) == set(constants.EXAMPLE_FILES + constants.DATA_FILES)
