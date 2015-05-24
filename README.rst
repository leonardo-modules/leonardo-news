
===============
News / Articles
===============

Adoptaion of ``feincms-articles`` for Leonardo CMS.

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install leonardo-news

optionaly install ``django-taggit``

.. code-block:: bash

    pip install leonardo-news[taggit]
    
    pip install django-taggit

or as leonardo bundle

.. code-block:: bash

    pip install django-leonardo["news"]

Add ``team`` to APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'news'
        ...
    ]

Run management commands

.. code-block:: bash

    python manage.py makemigrations --noinput
    python manage.py migrate --noinput

    python manage.py sync_all

Read More
---------

* https://github.com/django-leonardo/django-leonardo
* http://leonardo.robotice.org
* https://github.com/incuna/feincms-articles
