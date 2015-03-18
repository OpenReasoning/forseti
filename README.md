#Forseti
[![Build Status](https://travis-ci.org/MasterOdin/Forseti.svg?branch=master)](https://travis-ci.org/MasterOdin/Forseti) [![Coverage Status](https://coveralls.io/repos/MasterOdin/Forseti/badge.svg?branch=master)](https://coveralls.io/r/MasterOdin/Forseti?branch=master)

A Formal Logic framework for a variety of applications.

##Usage
Forseti comes with an internal representation of propositional calculus formulas (atomic, not, and, or, implication, and equivalance). It can generate this from a functional representation of any formula. Interally, it holds everything as a "Predicate" object, which can take in other Predicates as appropriate (Atomics can only hold one string).

An example:
```python
from forseti import parser
from forseti.predicate import Atomic, And
assert parser.parse(and(a, b)) == And(Atomic('a'), Atomic('b'))
```