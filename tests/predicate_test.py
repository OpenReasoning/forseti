"""
Tests to ensure that Predicate representation works as expected
"""
__author__ = 'mpeveler'

from forseti.predicate import Atomic, Not, And, Or, Implies, Equiv


def test_atomic():
    """
    Ensure Atomic Predicate is displayed properly
    """
    pred = Atomic('a')
    assert pred.get_print() == "a"
    assert pred.get_pretty_print() == "a"


def test_not():
    """
    Ensure Not Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_not = Not(pred_a)
    assert pred_not.get_print() == "not(a)"
    assert pred_not.get_pretty_print() == "~a"


def test_and():
    """
    Ensure And Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_and = And(pred_a, pred_b)
    assert pred_and.get_print() == "and(a, b)"
    assert pred_and.get_pretty_print() == "(a & b)"


def test_or():
    """
    Ensure Or Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_or = Or(pred_a, pred_b)
    assert pred_or.get_print() == "or(a, b)", pred_or.get_print()
    assert pred_or.get_pretty_print() == "(a | b)"


def test_implies():
    """
    Ensure Implies Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_implies = Implies(pred_a, pred_b)
    assert pred_implies.get_print() == "implies(a, b)"
    assert pred_implies.get_pretty_print() == "(a -> b)"


def test_equiv():
    """
    Ensure Equiv Predicate is displayed properly
    """
    pred_a = Atomic('a')
    pred_b = Atomic('b')
    pred_equiv = Equiv(pred_a, pred_b)
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
