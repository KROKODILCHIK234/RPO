
mtracker
========

Decorator to trace the memory use.


.. image:: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
   :target: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
   :alt: Python



.. image:: https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge
   :target: ./LICENSE
   :alt: Licence


Table Of Content
----------------


* `Description <#description>`_
* `Installation <#installation>`_
* `Testing <#Testing>`_
* `License <#license>`_

Description
===========

Use it to track the memory used by functions in your code. This project is a part of FOSS course and placed here to show how we can build library out of our code. 

Testing
=======

Get `pytest <https://docs.pytest.org/en/7.2.x/>`_

.. code-block::

   git clone git@github.com:standlab/mtracker.git
   cd mtracker
   pytest


Installation
============

Make sure `git <https://git-scm.com/>`_ is installed on your system. In bash-shell execute:

.. code-block::

   git clone git@github.com:standlab/mtracker.git
   cd mtracker
   pip install .


Or simply:

.. code-block::

   pip install git+https://github.com/standlab/mtracker.git#egg=mtracker


Remove the matracker:

.. code-block::

   pip uninstall mtracker


Contribute
==========

You can contribute to the project by writing more tests and check memory tracking with fancy data structures such as Pandas dataframes.

License
=======

The mtracker is licensed under the terms of the MIT Open Source license and is available for free.
