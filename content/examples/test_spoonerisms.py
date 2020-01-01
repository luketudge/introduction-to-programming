# -*- coding: utf-8 -*-
"""
Tests for the spoonerisms module.
"""

import pytest

import spoonerisms


def test_find_first_vowel():

    result = spoonerisms.find_first_vowel('smart')

    assert result == 2


def test_spoonerize():

    result = spoonerisms.spoonerize('four parts')

    assert result == 'pour farts'


def test_spoonerize_with_multiple_consonants():

    result = spoonerisms.spoonerize('smart fella')

    assert result == 'fart smella'


def test_spoonerize_with_initial_vowel():

    result = spoonerisms.spoonerize('arty farce')

    assert result == 'farty arce'


def test_spoonerize_exception():

    # Note: match='3' because the error message should mention
    # the number of words in the input string.
    with pytest.raises(ValueError, match='3'):
        spoonerisms.spoonerize('very smart fella')
