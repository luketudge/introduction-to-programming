# -*- coding: utf-8 -*-

import time

import pytest

from . import constants


@pytest.mark.parametrize('page', constants.TOPIC_PAGES)
@pytest.mark.parametrize('version', [constants.LOCAL_URL, constants.REMOTE_URL])
def test_topic_pages(browser, version, page):

    browser.get(version)
    browser.find_element_by_link_text(page).click()

    # Did we get the page?

    assert page in browser.page_source

    # Do the links in the table of contents actually take us to page sections?
    # (This turns out to be fairly difficult to test.
    # The hack here is to take a screenshot, click the link, take another,
    # then check whether the first n bytes of teh images are different.)

    time.sleep(constants.PAGE_WAIT)
    top_screenshot = browser.get_screenshot_as_base64()
    top_screenshot = top_screenshot[:constants.IMAGE_BYTES]

    for item in browser.find_elements_by_class_name('toc-item'):

        link = item.find_element_by_tag_name('a')
        link.click()
        new_screenshot = browser.get_screenshot_as_base64()
        new_screenshot = new_screenshot[:constants.IMAGE_BYTES]

        assert new_screenshot != top_screenshot, 'TOC failed: {}'.format(link.text)
