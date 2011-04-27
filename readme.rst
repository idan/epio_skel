epio_skel - A skeleton Django project for ep.io
===============================================

Getting started with ep.io is not a daunting task, but setting up a good project structure requires a thousand little tweaks to get "just right."

This skeleton project is my project base for working with ep.io. It provides:

* A settings module which provides for epio-specific settings without getting
  in your way during development.
* Caching via redis -- ep.io does not have memcached. Relies on sebleier's
  excellent django-redis-cache_. You'll still need to enable per-site/per-view
  caching on your own if you desire it.
* A sensible ``epio.ini``.
* A sensible ``.gitignore``.
* ``PYTHONPATH`` settings which conform to epio's suggested best-practices_:
  the project dir is on ``PYTHONPATH``, so you import things from ``app.foo``,
  not ``project.app.foo``.

.. _django-redis-cache: https://github.com/sebleier/django-redis-cache
.. _best-practices: http://www.ep.io/docs/guides/django/#project-names-in-imports

How do I use this?
==================

Download the project skeleton. If you've cloned the project, you'll probably want to remove the .git directory first.

Create a virtualenv for your project. You *are* using virtualenv, right?

Install some basic requirements using ``pip install -r requirements.txt``. You *are* using pip, right?

You'll need to specify a value for ``SECRET_KEY`` in ``settings/base.py``. By default, Django concocts a random 50-character alphanumeric string for this value.

You'll also probably want to add ``settings/local.py`` to your ``.gitignore``. It isn't that way out of the box because I wanted to include an example local.py.

An aside on the settings module
-------------------------------

The settings module separates settings into three files by default:

base.py
    The base settings file. Settings that apply to all environments (epio, development, etc) should go here. All other settings files should import from `base.py` at the top of the file. 

epio.py
    Settings specific to ep.io. This settings file will only be loaded if there's an ``EPIO`` environment variable set -- which is taken care of by
    ``epio.ini``. Put any epio-specific settings here.

local.py
    If this file is present and the ``EPIO`` envvar is not set, it is imported. This is a good place to put development-related settings. Note that for this scheme to work, you must retain the import at the top of the
    file. The supplied example local.py includes some common settings you'll
    want to fill in for local work.

Here, have a handy-dandy l33t ASCII-art flowchart::

    * Start Here! *
    ---------------         ---------------         -----------
    | Is EPIO     | --no--> | Is local.py | --no--> | base.py |
    | envvar set? |         | present?    |         -----------
    ---------------         ---------------               ^  
           |                       |                      |
          yes                     yes                     |
           |                       |                      |
           v                       v                      |
      -----------             ------------                |
      | epio.py |             | local.py |                |
      -----------             ------------                |
           |                       |                      |
           \-----------------------\---- imports * from --/

That should be it! Happy epio'ing.