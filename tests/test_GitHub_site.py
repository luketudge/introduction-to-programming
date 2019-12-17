# -*- coding: utf-8 -*-

TOPIC_PAGE = 'Topic listing'

TOPICS = ['Creating a computer program with Python',
          'Variables and data types',
          'Sequences and mappings',
          'Conditions',
          'Iteration',
          'Functions',
          'Modules',
          'The standard library',
          'Files']


def test_topic_pages(browser):

    # Do we get the main page?
    assert 'introduction-to-programming' in browser.title

    # Navigate to the topics page.
    topics_link = browser.find_element_by_link_text(TOPIC_PAGE)
    topics_link.click()

    # Visit each of the topic pages.
    for topic in TOPICS:

        topic_link = browser.find_element_by_link_text(topic)
        topic_link.click()

        # Did we get it?
        assert topic in browser.page_source

        # Does it have a table of contents?
        assert 'Contents' in browser.page_source

        # Go back.
        browser.back()
