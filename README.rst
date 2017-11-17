forseti
=======

.. image:: https://travis-ci.org/OpenReasoning/forseti.svg?branch=master
    :target: https://travis-ci.org/OpenReasoning/forseti
    :alt: Build Status
.. image:: https://coveralls.io/repos/OpenReasoning/forseti/badge.svg?branch=master
    :target: https://coveralls.io/r/OpenReasoning/forseti?branch=master
    :alt: Coverage Status
.. image:: https://landscape.io/github/OpenReasoning/forseti/master/landscape.svg?style=flat
    :target: https://landscape.io/github/OpenReasoning/forseti/master
    :alt: Code Health

A Formal Logic framework for a variety of applications.

Installation
~~~~~~~~~~~~

From PyPI
~~~~~~~~~
forseti is available on `PyPI <https://pypi.python.org/pypi/forseti>`_.

::

    $ pip install forseti

From source
~~~~~~~~~~~
* Download the source code:

::

    $ git clone git@github.com:OpenReasoning/forseti.git
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
  assert parser.parse("and(a, b)") == And(Atomic('a'), Atomic('b'))

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

Usages
------
These projects use forseti at their core:

1. `Truth Tables <https://github.com/OpenReasoning/TruthTables>`_

Goals
-----
Using forseti to implement the following programs/applications

1. Automated Theorem Prover (done in forseti core)
2. `Implement Davis-Putnam Algorithm <http://en.wikipedia.org/wiki/Davis%E2%80%93Putnam_algorithm>`_
3. `Truth Trees <http://legacy.earlham.edu/~peters/courses/log/treeprop.htm>`_
4. `Slate <http://rair.cogsci.rpi.edu/projects/slate/>`_ / `Fitch <http://en.wikipedia.org/wiki/Fitch-style_calculus>`_
