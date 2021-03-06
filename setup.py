#!/usr/bin/env python3

import os
from setuptools import setup

from djexcept import __version__


def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "djexcept",
    version = __version__,
    description = "Flexible and versatile exception handling for django.",
    long_description = read_file("README.rst"),
    url = "https://github.com/efficiosoft/djexcept",
    author = "Robert Schindler",
    author_email = "r.schindler@efficiosoft.com",
    license = "GPL-3",
    packages = ["djexcept"],
    install_requires = ["django"],
    zip_safe = False,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
