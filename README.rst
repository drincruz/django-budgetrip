================================
django-budgetrip example project
================================

This project shows how to use django to show a dashboard for money saved from budget for trips using Python + Django

.. note ::

    This does **not** include bigger picture modules such as: user login, metrics reporting, et cetera.

.. contents::

All code is MIT licensed.

-----------------------------------------------
Prerequisitements
-----------------------------------------------

In order to run this app, you need to have mastered

* Python 2.7

* `virtualenv <http://opensourcehacker.com/2012/09/16/recommended-way-for-sudo-free-installation-of-python-software-with-virtualenv>`_

* Django basics: how to configure Django project, MySQL, models, South migrations, using interactive Python shell.

-----------------------------------------------
Installation
-----------------------------------------------

Installation (`virtualenv based <http://opensourcehacker.com/2012/09/16/recommended-way-for-sudo-free-installation-of-python-software-with-virtualenv/>`_)::

    git clone git@github.com:drincruz/django-budgetrip-example.git
    cd django-budgetrip-example
    virtualenv venv   # Create virtualenv folder caller venv
    . env/bin/activate  # Activate virtualenv

Install Python dependencies using *pip*::

    pip install -r requirements.txt

Initializing database
==========================

``django-bitcoin`` uses South for its schema management.
Create a database (sqlite ``test.db`` file by default)::

    python manage.py syncdb
    python manage.pt migrate budgets

Do a test run
=================

Let's open the development web server and see that the Django admin is up with ``django-budgetrip``::

    python manage.py runserver

Visit ``http://localhost:8000/`` to see the Django budgetrip interface.

And that's it!

-----------------------------------------------
Author
-----------------------------------------------

Adrian Cruz(`blog <http://drincruz.com>`_, `Twitter <https://twitter.com/drincruz`_, `Google+ <https://plus.google.com/u/0/+AdrianCruz0`_)

