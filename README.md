#forseti
[![Build Status](https://travis-ci.org/MasterOdin/forseti.svg?branch=master)](https://travis-ci.org/MasterOdin/forseti) 
[![Coverage Status](https://coveralls.io/repos/MasterOdin/forseti/badge.svg?branch=master)](https://coveralls.io/r/MasterOdin/forseti?branch=master) 
[![Code Health](https://landscape.io/github/MasterOdin/forseti/master/landscape.svg?style=flat)](https://landscape.io/github/MasterOdin/forseti/master)
[![Latest Version](https://pypip.in/version/forseti/badge.svg)](https://pypi.python.org/pypi/forseti/)
[![Development Status](https://pypip.in/status/forseti/badge.svg)](https://pypi.python.org/pypi/forseti/)
[![Supported Python versions](https://pypip.in/py_versions/forseti/badge.svg)](https://pypi.python.org/pypi/forseti/)
[![License](https://pypip.in/license/forseti/badge.svg)](https://pypi.python.org/pypi/forseti/)

A Formal Logic framework for a variety of applications.

##Usage
forseti comes with an internal representation of propositional calculus formulas (atomic, not, and, or, implication, and equivalance). 
It can generate this from a functional representation of any formula. Interally, it holds everything as formula objects, which 
can take in other formulas as appropriate (Symbols can only hold one string).

An example:
```python
from forseti import parser
from forseti.predicate import Atomic, And
assert parser.parse(and(a, b)) == And(Atomic('a'), Atomic('b'))
```

Additionally, it also comes with a builtin prover that can validate a propositional calculus argument
```python
from forseti.prover import Prover
prover = Prover()
prover.add_formula("if(A,and(B,C))")
prover.add_formula("iff(C,B)")
prover.add_formula("not(C)")
prover.add_goal("not(A)")
assert_true(prover.run_prover())
```

##Roadmap:
1. Formal Logic Prover
1. Optimizations

##Goals:
Using forseti to implement the following programs/applications  

1. Automated Theorem Prover (done in forseti core)  
1. [Implement Davis-Putnam Algorithm](http://en.wikipedia.org/wiki/Davis%E2%80%93Putnam_algorithm)  
1. [Truth Trees](http://legacy.earlham.edu/~peters/courses/log/treeprop.htm)  
1. [Slate](http://rair.cogsci.rpi.edu/projects/slate/)/[Fitch](http://en.wikipedia.org/wiki/Fitch-style_calculus)  
