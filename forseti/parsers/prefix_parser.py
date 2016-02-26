"""
Module that contains a prefix parser for formulas

Acceptable statements are of the form:
A
(not A)
(and A B)
(or A B)
(if A B)
(iff A B)
"""

from __future__ import unicode_literals
from forseti.formula import Symbol, Not, And, Or, If, Iff, Predicate, \
    Existential, Universal
from forseti.parsers.abstract_parser import AbstractParser


class PrefixParser(AbstractParser):
    @staticmethod
    def parse(statement, formula_types):
        raise NotImplementedError("Not Implemented Error")