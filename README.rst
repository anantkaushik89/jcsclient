========
Overview
========

.. .. start-badges
..
.. .. list-table::
..     :stub-columns: 1
..
..     * - docs
..       - |docs|
..     * - tests
..       - |
..         | |codecov|
..     * - package
..       - |version| |downloads| |wheel| |supported-versions| |supported-implementations|
..
.. .. |docs| image:: https://readthedocs.org/projects/client/badge/?style=flat
..     :target: https://readthedocs.org/projects/client
..     :alt: Documentation Status
..
.. .. |codecov| image:: https://codecov.io/github/jiocloudservices/client/coverage.svg?branch=master
..     :alt: Coverage Status
..     :target: https://codecov.io/github/jiocloudservices/client
..
.. .. |version| image:: https://img.shields.io/pypi/v/client.svg?style=flat
..     :alt: PyPI Package latest release
..     :target: https://pypi.python.org/pypi/client
..
.. .. |downloads| image:: https://img.shields.io/pypi/dm/client.svg?style=flat
..     :alt: PyPI Package monthly downloads
..     :target: https://pypi.python.org/pypi/client
..
.. .. |wheel| image:: https://img.shields.io/pypi/wheel/client.svg?style=flat
..     :alt: PyPI Wheel
..     :target: https://pypi.python.org/pypi/client
..
.. .. |supported-versions| image:: https://img.shields.io/pypi/pyversions/client.svg?style=flat
..     :alt: Supported versions
..     :target: https://pypi.python.org/pypi/client
..
.. .. |supported-implementations| image:: https://img.shields.io/pypi/implementation/client.svg?style=flat
..     :alt: Supported implementations
..     :target: https://pypi.python.org/pypi/client
..
..
.. .. end-badges

Client library for JCS

Installation
============

.. pip install client

Installation from source
-----------------------

::

    git clone https://github.com/jiocloudservices/jcsclient.git
    cd jcsclient
    sudo pip install -r requirements.txt   # Can use virtual environment too
    sudo python setup.py develop

Installation as a pip package
-----------------------

::

    pip install -e git+https://github.com/jiocloudservices/jcsclient.git#egg=jcsclient

Configuration
=============

Copy openrc.sample to create `openrc` file, put your actual credentials in this
file and then source this file Edit the src/client/config.py to include your
credentials.

::

    cp openrc.sample openrc
    # Update openrc now, and add your access/secret keys
    source openrc

If you are from your local machine, you might need to add entries to `/etc/hosts` file to map an IP to the endpoint. No need to do the same if you are using this library from a staging machien.

**NOTE**: Never ever commit your access and secret keys and push to a public repository. You have been warned.


CLI
===

You can use CLI to make an API request, or just get the input which you can use with 'curl' command.

::

    $ jcs compute describe-instances

First argument is service name (one of 'compute', 'vpc', 'dss', 'iam' and 'rds'). To get help on a service, execute:

::

    jcs <service> --help

To get helptext for a particular command, execute:

::

    jcs <service> <command> --help

.. To run the all tests run::
..
..     tox
..
.. Note, to combine the coverage data from all the tox environments run:
..
.. .. list-table::
..     :widths: 10 90
..     :stub-columns: 1
..
..     - - Windows
..       - ::
..
..             set PYTEST_ADDOPTS=--cov-append
..             tox
..
..     - - Other
..       - ::
..
..             PYTEST_ADDOPTS=--cov-append tox
