# -*- coding: utf-8 -*-

import pytest

from . import constants


@pytest.mark.parametrize('page', constants.TOPIC_PAGES)
@pytest.mark.parametrize('version', [constants.LOCAL_URL, constants.REMOTE_URL])
def test_topic_pages(browser, version, page):

    # Load the main page.
    browser.get(version)

    # Visit one of the topic pages.
    link = browser.find_element_by_link_text(page)
    link.location_once_scrolled_into_view
    link.click()

    # Did we get it?
    assert page in browser.page_source
