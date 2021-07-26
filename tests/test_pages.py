# -*- coding: utf-8 -*-

import pytest

from . import constants


def click_link(link):

    link.location_once_scrolled_into_view
    link.click()


@pytest.mark.parametrize('page', constants.TOPIC_PAGES)
@pytest.mark.parametrize('version', [constants.LOCAL_URL, constants.REMOTE_URL])
def test_topic_pages(browser, version, page):

    browser.get(version)

    # Visit one of the topic pages.
    link = browser.find_element_by_link_text(page)
    click_link(link)

    # Did we get it?
    assert page in browser.page_source


@pytest.mark.parametrize('version', [constants.LOCAL_URL, constants.REMOTE_URL])
def test_example_program_link(browser, version):

    browser.get(version)

    # Visit the first topic page.
    link = browser.find_element_by_link_text(constants.INTRO_PAGE)
    click_link(link)

    # Click the first link to an example program.
    link = browser.find_element_by_link_text(constants.INTRO_EXAMPLE)
    click_link(link)
