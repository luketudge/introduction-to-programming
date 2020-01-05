# -*- coding: utf-8 -*-
"""
Test that mathematics is working as normal in your current working universe.
"""

import pytest


def test_two_plus_two_equals_four():

    assert 2 + 2 == 4


def test_division_by_zero_is_undefined():

    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
