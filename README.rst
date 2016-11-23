========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/psr-generator/badge/?style=flat
    :target: https://readthedocs.org/projects/psr-generator
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/benbaror/psr-generator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/benbaror/psr-generator

.. |requires| image:: https://requires.io/github/benbaror/psr-generator/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/benbaror/psr-generator/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/benbaror/psr-generator/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/benbaror/psr-generator

.. |codecov| image:: https://codecov.io/github/benbaror/psr-generator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/benbaror/psr-generator

.. |version| image:: https://img.shields.io/pypi/v/psr-generator.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/psr-generator

.. |downloads| image:: https://img.shields.io/pypi/dm/psr-generator.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/psr-generator

.. |wheel| image:: https://img.shields.io/pypi/wheel/psr-generator.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/psr-generator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/psr-generator.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/psr-generator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/psr-generator.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/psr-generator


.. end-badges

Modelling of the Galactic radio pulsar population

* Free software: BSD license

Installation
============

::

    pip install psr-generator

Documentation
=============

https://psr-generator.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
