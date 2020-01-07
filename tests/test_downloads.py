# -*- coding: utf-8 -*-

from . import constants


def test_download_examples(file):

    contents = file.namelist()

    assert set(contents) == set(constants.EXAMPLE_FILES + constants.DATA_FILES)
