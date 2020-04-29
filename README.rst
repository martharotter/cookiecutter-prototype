Cookiecutter Django
=======================

Powered by Cookiecutter_, this personal cookiecutter is my base framework for jumpstarting
Django-based proofs-of-concept and prototypes quickly.

Features
---------

* For Django 3.0.5
* Works with Python 3.8
* Renders Django projects with 100% starting test coverage
* Twitter Bootstrap_ v4
* 12-Factor_ based settings via django-environ_
* Optimized for fast development settings
* Comes with custom user model ready to go
* Optional custom static build using livereload
* Docker support using docker-compose_ for development and production (using Traefik_ with LetsEncrypt_ support)
* Run tests with unittest or pytest
* Default integration with pre-commit_ for identifying simple issues before submission to code review


Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

.. _Bootstrap: https://github.com/twbs/bootstrap
.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _docker-compose: https://github.com/docker/compose
.. _pre-commit: https://github.com/pre-commit/pre-commit 

Constraints
-----------

* Only maintained 3rd party libraries are used.
* Uses SQLite everywhere
* Environment variables for configuration (This won't work with Apache/mod_wsgi).

Usage
------

Let's pretend you want to prototype a concept called "redditclone". Rather than using ``startproject`` and then 
editing the results to include your name, email, and various configuration issues that always get forgotten 
until the worst possible moment, get cookiecutter_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.7.2"

Now run it against this repo::

    $ cookiecutter https://github.com/martharotter/cookiecutter-prototype

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Martha Rotter', 'martharotter', etc to your own information.

Answer the prompts with your own desired options_. For example::

    Cloning into 'cookiecutter-prototype'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [Project Name]: Reddit Clone
    project_slug [reddit_clone]: reddit
    author_name [Martha Rotter]: Martha Rotter
    email [you@example.com]: martharotter@gmail.com
    description [Behold My Awesome Project!]: A reddit clone.
    domain_name [example.com]: myreddit.com
    version [0.1.0]: 0.0.1
    timezone [UTC]: Europe/Dublin
    use_docker [y]: y
    Choose from 1, 2, 3, 4, 5, 6 [1]: 1
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 1
    keep_local_envs_in_vcs [y]: y
    debug[y]: y

Enter the project and take a look around::

    $ cd reddit/
    $ ls

Create a git repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:martharotter/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

Code of Conduct
---------------

Everyone interacting in the Cookiecutter project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.


.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
