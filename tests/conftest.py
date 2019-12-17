# -*- coding: utf-8 -*-

import os
import zipfile


import pytest
import requests
from selenium import webdriver


# %% Paths

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

TEMP_FILENAME = os.path.join(BASE_PATH, 'temp.zip')


# %% URLs

URL = 'https://github.com/luketudge/introduction-to-programming/'
BRANCHES = ['master', 'in-progress']


# %% Helper function

def delete_temp_file():

    try:
        os.remove(TEMP_FILENAME)
    except FileNotFoundError:
        pass


# %% Fixtures

@pytest.fixture(params=BRANCHES)
def browser(request):

    fb = webdriver.Firefox()
    fb.get(URL + 'tree/' + request.param)

    yield fb

    fb.quit()


@pytest.fixture(params=BRANCHES)
def file(request):

    delete_temp_file()

    url = URL + 'blob/' + request.param + '/content/examples/intro_prog_examples.zip'
    r = requests.get(url, params={'raw': 'true'})

    with open(TEMP_FILENAME, mode='wb') as f:
        f.write(r.content)

    with zipfile.ZipFile(TEMP_FILENAME) as f:
        yield f

    delete_temp_file()
