# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():

    fb = webdriver.Firefox()

    yield fb

    fb.quit()
