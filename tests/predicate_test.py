# pylint: disable=missing-docstring
"""
Tests to ensure that Predicate representation works as expected
"""

from __future__ import print_function
from nose.tools import raises
from forseti.predicate import Predicate, Atomic, Not, And, Or, Implies, Equiv


@raises(NotImplementedError)
def test_abstract_argument_number():
    pred = Predicate()
    pred.argument_number()


@raises(NotImplementedError)
def test_abstract_get_print():
    pred = Predicate()
    pred.get_print()


@raises(NotImplementedError)
def test_abstract_get_pretty_print():
    pred = Predicate()
    pred.get_pretty_print()


@raises(NotImplementedError)
def test_abstract_print():
    pred = Predicate()
    str(pred)


@raises(TypeError)
def test_invalid_predicate():
    Predicate("a")


def test_atomic():
    pred = Atomic('a')
    assert pred.argument_number() == 1
    assert pred.get_print() == "a"
    assert pred.get_pretty_print() == "a"


def test_not():
    pred_a = Atomic('a')
    pred_not = Not(pred_a)
    assert pred_not.argument_number() == 1
    assert pred_not.get_print() == "not(a)"
    assert pred_not.get_pretty_print() == "~a"


def test_and():
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_and = And(pred_a, pred_b)
    assert pred_and.argument_number() == 2
    assert pred_and.get_print() == "and(a, b)"
    assert pred_and.get_pretty_print() == "(a & b)"


def test_or():
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_or = Or(pred_a, pred_b)
    assert pred_or.argument_number() == 2
    assert pred_or.get_print() == "or(a, b)", pred_or.get_print()
    assert pred_or.get_pretty_print() == "(a | b)"


def test_implies():
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_implies = Implies(pred_a, pred_b)
    assert pred_implies.argument_number() == 2
    assert pred_implies.get_print() == "implies(a, b)"
    assert pred_implies.get_pretty_print() == "(a -> b)"


def test_equiv():
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_equiv = Equiv(pred_a, pred_b)
    assert pred_equiv.argument_number() == 2
    assert pred_equiv.get_print() == "equiv(a, b)"
    assert pred_equiv.get_pretty_print() == "(a <-> b)"


def test_complex():
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_and = And(pred_a, pred_b)
    pred_or = Or(pred_and, pred_a)
    pred_implies = Implies(pred_or, pred_and)
    pred_equiv = Equiv(pred_implies, pred_a)
    assert pred_equiv.get_print() == "equiv(implies(or(and(a, b), a), " \
                                     "and(a, b)), a)"
    assert pred_equiv.get_pretty_print() == "((((a & b) | a) -> (a & b))" \
                                            " <-> a)"


def test_equality():
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_and = And(pred_a, pred_b)
    pred_or = Or(pred_and, pred_a)
    pred_implies = Implies(pred_or, pred_and)
    pred_equiv = Equiv(pred_implies, pred_a)
    assert pred_equiv == Equiv(Implies(Or(And(Atomic("a"), Atomic("b")),
                                          Atomic("a")), And(Atomic("a"),
                                                            Atomic("b"))),
                               Atomic("a"))


def test_non_equality():
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_and = And(pred_a, pred_b)
    pred_or = Or(pred_and, pred_b)
    assert pred_or != Or(And(Atomic('a'), Atomic('b')), Atomic('a'))


@raises(TypeError)
def test_bad_atomic():
    Atomic(Atomic('a'))
