# -*- coding: utf-8 -*-

import os
import zipfile

import pytest
import requests
from selenium import webdriver

from . import constants


# %% Helper functions

def delete_temp_file():

    try:
        os.remove(constants.TEMP_FILENAME)
    except FileNotFoundError:
        pass


# %% Fixtures

@pytest.fixture(scope='session')
def browser():

    fb = webdriver.Firefox()

    yield fb

    fb.quit()


@pytest.fixture(params=constants.BRANCHES)
def file(request):

    delete_temp_file()

    url = constants.REMOTE_URL + 'blob/' + request.param + '/content/examples/intro_prog_examples.zip'
    r = requests.get(url, params={'raw': 'true'})

    with open(constants.TEMP_FILENAME, mode='wb') as f:
        f.write(r.content)

    with zipfile.ZipFile(constants.TEMP_FILENAME) as f:
        yield f

    delete_temp_file()
