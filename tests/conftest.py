# -*- coding: utf-8 -*-

import pytest
from selenium.webdriver.firefox.webdriver import WebDriver


URL = 'https://github.com/luketudge/introduction-to-programming/tree/'
BRANCHES = ['master', 'in-progress']


@pytest.fixture(params=BRANCHES)
def browser(request):

    browser = WebDriver()
    browser.get(URL + request.param)

    yield browser

    browser.quit()
