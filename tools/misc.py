# -*- coding: utf-8 -*-
"""
Miscellaneous additional tools.
"""

import glob
import itertools
import os
import zipfile


def strip_extension(filename):
    """Strip the file extension from a filename.
    """
    
    return filename.rsplit('.', 1)[0]


def zip_all(destination, path='.', patterns=('**',)):
    """Put multiple files into a zip archive.

    Arguments:
        destination: destination filename
        path: path on which to search for files to zip
        patterns: iterable of glob-style filename patterns to search for

    Example:
        >>> # zip all .py and .md files in directory my_dir to my_zip.zip
        >>> zip_all('my_zip.zip', path='my_dir', patterns=['*.py', '*.md'])
    """

    filenames = [glob.glob(os.path.join(path, p)) for p in patterns]

    with zipfile.ZipFile(destination, mode='w') as zf:
        for f in itertools.chain(*filenames):
            arcname = f[len(path)+1:]
            zf.write(f, arcname=arcname)
