forseti
=======

.. image:: https://travis-ci.org/MasterOdin/forseti.svg?branch=master
    :target: https://travis-ci.org/MasterOdin/forseti
    :alt: Build Status
.. image:: https://coveralls.io/repos/MasterOdin/forseti/badge.svg?branch=master
    :target: https://coveralls.io/r/MasterOdin/forseti?branch=master
    :alt: Coverage Status
.. image:: https://landscape.io/github/MasterOdin/forseti/master/landscape.svg?style=flat
    :target: https://landscape.io/github/MasterOdin/forseti/master
    :alt: Code Health
.. image:: https://pypip.in/version/forseti/badge.svg
    :target: https://pypi.python.org/pypi/forseti/
    :alt: Latest Version
.. image:: https://pypip.in/status/forseti/badge.svg
    :target: https://pypi.python.org/pypi/forseti/
    :alt: Development Status
.. image:: https://pypip.in/py_versions/forseti/badge.svg
    :target: https://pypi.python.org/pypi/forseti/
    :alt: Supported Python versions
.. image:: https://pypip.in/license/forseti/badge.svg
    :target: https://pypi.python.org/pypi/forseti/
    :alt: License

A Formal Logic framework for a variety of applications.

Installation
------------

From PyPI
~~~~~~~~~
forseti is available on `PyPI <https://pypi.python.org/pypi/forseti>`_.

::

    $ pip install forseti

From source
~~~~~~~~~~~
* Download the source code:

::

    $ git clone git@github.com:MasterOdin/forseti.git
    $ python setup.py install

Usage
-----

forseti comes with an internal representation of propositional calculus formulas (atomic, not, and, or, implication, and equivalance).
It can generate this from a functional representation of any formula. Interally, it holds everything as formula objects, which
can take in other formulas as appropriate (Symbols can only hold one string).

An example:

.. code-block:: python

  from forseti import parser
  from forseti.predicate import Atomic, And
  assert parser.parse(and(a, b)) == And(Atomic('a'), Atomic('b'))

Additionally, it also comes with a builtin prover that can validate a propositional calculus argument

.. code-block:: python

    from forseti.prover import Prover
    prover = Prover()
    prover.add_formula("if(A,and(B,C))")
    prover.add_formula("iff(C,B)")
    prover.add_formula("not(C)")
    prover.add_goal("not(A)")
    assert_true(prover.run_prover())

Roadmap
-------
1. First Order Logic Prover
2. Optimizations

Goals
-----
Using forseti to implement the following programs/applications

1. Automated Theorem Prover (done in forseti core)
2. `Implement Davis-Putnam Algorithm <http://en.wikipedia.org/wiki/Davis%E2%80%93Putnam_algorithm>`_
3. `Truth Trees <http://legacy.earlham.edu/~peters/courses/log/treeprop.htm>`_
4. `Slate <http://rair.cogsci.rpi.edu/projects/slate/>`_ / `Fitch <http://en.wikipedia.org/wiki/Fitch-style_calculus>`_