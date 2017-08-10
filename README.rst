===============================
freshbook
===============================


.. .. image:: https://img.shields.io/pypi/v/freshbook.svg
        :target: https://pypi.python.org/pypi/freshbook

.. .. image:: https://img.shields.io/travis/redraw/freshbook.svg
        :target: https://travis-ci.org/redraw/freshbook

.. .. image:: https://readthedocs.org/projects/freshbook/badge/?version=latest
        :target: https://freshbook.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. .. image:: https://pyup.io/repos/github/redraw/freshbook/shield.svg
     :target: https://pyup.io/repos/github/redraw/freshbook/
     :alt: Updates


Freshbooks hours logger tool

Installation
----

``$ pip install freshbook``

Use
----

First, create the config file by running

``$ freshbook init``

This creates a file named ``.freshbook`` in the current project directory. When you're ready to log, make sure you're on the same directory and run,

``$ freshbook commit -m "the message"``

Git
----

If using git, you could use your commit messages to include in the freshbook notes.

``$ git config --global alias.today "log --author '`git config user.name`' --since 6am --all --no-merges --format='-%s'"``

And then just do

``$ freshbook commit -m "$(git today)"``
