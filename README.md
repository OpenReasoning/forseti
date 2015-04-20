#Forseti
[![Build Status](https://travis-ci.org/MasterOdin/Forseti.svg?branch=master)](https://travis-ci.org/MasterOdin/Forseti) 
[![Coverage Status](https://coveralls.io/repos/MasterOdin/Forseti/badge.svg?branch=master)](https://coveralls.io/r/MasterOdin/Forseti?branch=master) 
[![Latest Version](https://pypip.in/version/Forseti/badge.svg)](https://pypi.python.org/pypi/Forseti/)
[![Development Status](https://pypip.in/status/Forseti/badge.svg)](https://pypi.python.org/pypi/Forseti/)
[![Supported Python versions](https://pypip.in/py_versions/Forseti/badge.svg)](https://pypi.python.org/pypi/Forseti/)
[![License](https://pypip.in/license/Forseti/badge.svg)](https://pypi.python.org/pypi/Forseti/)

A Formal Logic framework for a variety of applications.

##Usage
Forseti comes with an internal representation of propositional calculus formulas (atomic, not, and, or, implication, and equivalance). It can generate this from a functional representation of any formula. Interally, it holds everything as a "Predicate" object, which can take in other Predicates as appropriate (Atomics can only hold one string).

An example:
```python
from forseti import parser
from forseti.predicate import Atomic, And
assert parser.parse(and(a, b)) == And(Atomic('a'), Atomic('b'))
```

##Goals:
Using Forseti to implement the following programs/applications  

1. Automated Theorem Prover (done in Forseti core)  
1. [Implement Davis-Putnam Algorithm](http://en.wikipedia.org/wiki/Davis%E2%80%93Putnam_algorithm)  
1. [Truth Trees](http://legacy.earlham.edu/~peters/courses/log/treeprop.htm)  
1. [Slate](http://rair.cogsci.rpi.edu/projects/slate/)/[Fitch](http://en.wikipedia.org/wiki/Fitch-style_calculus)  
