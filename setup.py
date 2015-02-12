# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from yaml2rst import __version__

long_description = "\n\n".join([
    open("README.rst").read(),
    ])

setup(
    name="yaml2rst",
    version=__version__,
    description="""A Simple Tool for Documenting YAML Files""",
    long_description=long_description,
    author="Hartmut Goebel",
    author_email='h.goebel@crazy-compilers.com',
    license="GPLv3+",
    py_modules = ['yaml2rst'],
    scripts=['bin/yaml2rst'],
    #url="",
    #download_url='http://yml2rst-%s.tar.gz' % __version__,
    keywords=['YML', 'rst', 'reStructuresText', 'literate programming'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Documentation :: Sphinx',
    ],
)
