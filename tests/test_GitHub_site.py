# -*- coding: utf-8 -*-


def test_main_page(browser):

    assert 'introduction-to-programming' in browser.title
