#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'docopt==0.6.2',
    'six==1.10.0',
    'refreshbooks==2.0'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='freshbook',
    version='0.1.0',
    description="Freshbooks hours logger tool",
    long_description=readme + '\n\n' + history,
    author="agustin",
    author_email='agustinbv@gmail.com',
    url='https://github.com/redraw/freshbook',
    packages=[
        'freshbook',
    ],
    package_dir={'freshbook':
                 'freshbook'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='freshbook',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': ['freshbook=freshbook.cli:main']
    }
)
