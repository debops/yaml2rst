# -*- coding: utf-8 -*-

from setuptools import setup

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
    packages=['yaml2rst'],
    url="https://github.com/htgoebel/yaml2rst",
    # These are for reference only, pip is not able to download packages
    # from github because the archives do not include the project-name.
    download_url="https://github.com/htgoebel/yaml2rst/releases",
    bugtrack_url="https://github.com/htgoebel/yaml2rst/issues",
    keywords=['YML', 'YAML',
              'rst', 'reStructuresText',
              'literate programming'],
    entry_points={
        'console_scripts': [
            'yaml2rst = yaml2rst.__main__:run',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Documentation',
    ],
)
