"""
Tests to ensure that Predicate representation works as expected
"""

from __future__ import print_function
from nose.tools import raises
from forseti.predicate import Predicate, Atomic, Not, And, Or, Implies, Equiv

@raises(NotImplementedError)
def test_abstract_argument_number():
    """
    Test that Predicate abstract class throws error on argument_number()
    """
    pred = Predicate()
    pred.argument_number()


@raises(NotImplementedError)
def test_abstract_get_print():
    """
    Test that Predicate abstract class throws error on get_print()
    """
    pred = Predicate()
    pred.get_print()


@raises(NotImplementedError)
def test_abstract_get_pretty_print():
    """
    Test that Predicate abstract class throws error on get_pretty_print()
    """
    pred = Predicate()
    pred.get_pretty_print()


@raises(NotImplementedError)
def test_abstract_print():
    """
    Test that Predicate abstract class throws error on __str__()
    """
    pred = Predicate()
    str(pred)


@raises(TypeError)
def test_invalid_predicate():
    """
    Test that Predicate abstract class throws TypeError on using non Predicates
    as arguments
    """
    Predicate("a")


def test_atomic():
    """
    Ensure Atomic Predicate is displayed properly
    """
    pred = Atomic('a')
    assert pred.argument_number() == 1
    assert pred.get_print() == "a"
    assert pred.get_pretty_print() == "a"


def test_not():
    """
    Ensure Not Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_not = Not(pred_a)
    assert pred_not.argument_number() == 1
    assert pred_not.get_print() == "not(a)"
    assert pred_not.get_pretty_print() == "~a"


def test_and():
    """
    Ensure And Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_and = And(pred_a, pred_b)
    assert pred_and.argument_number() == 2
    assert pred_and.get_print() == "and(a, b)"
    assert pred_and.get_pretty_print() == "(a & b)"


def test_or():
    """
    Ensure Or Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_or = Or(pred_a, pred_b)
    assert pred_or.argument_number() == 2
    assert pred_or.get_print() == "or(a, b)", pred_or.get_print()
    assert pred_or.get_pretty_print() == "(a | b)"


def test_implies():
    """
    Ensure Implies Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_implies = Implies(pred_a, pred_b)
    assert pred_implies.argument_number() == 2
    assert pred_implies.get_print() == "implies(a, b)"
    assert pred_implies.get_pretty_print() == "(a -> b)"


def test_equiv():
    """
    Ensure Equiv Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_equiv = Equiv(pred_a, pred_b)
    assert pred_equiv.argument_number() == 2
    assert pred_equiv.get_print() == "equiv(a, b)"
    assert pred_equiv.get_pretty_print() == "(a <-> b)"


def test_complex():
    """
    Ensure a complex predicate with multiple parts is displayed properly
    """
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
