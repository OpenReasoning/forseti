"""
Tests to ensure that LogicalOperator representation works as expected
"""
# pylint: disable=missing-docstring,expression-not-assigned

from __future__ import unicode_literals
from nose import runmodule
from nose.tools import raises, assert_equal, assert_true, assert_not_equal, \
    assert_false, assert_less, assert_greater, assert_greater_equal, \
    assert_less_equal, assert_is_not_none
from forseti.formula import Formula, Symbol, LogicalOperator, Not, And, Or, \
    If, Iff


@raises(NotImplementedError)
def test_formula_str():
    str(Formula())


@raises(NotImplementedError)
def test_formula_repr():
    repr(Formula())


@raises(NotImplementedError)
def test_formula_eq():
    Formula() == Formula()


@raises(NotImplementedError)
def test_formula_ne():
    Formula() != Formula()


@raises(NotImplementedError)
def test_formula_lt():
    Formula() < Formula()


@raises(NotImplementedError)
def test_formula_le():
    Formula <= Formula()


@raises(NotImplementedError)
def test_formula_gt():
    Formula() > Formula()


@raises(NotImplementedError)
def test_formula_ge():
    Formula >= Formula()


@raises(NotImplementedError)
def test_formula_hash():
    hash(Formula())


@raises(NotImplementedError)
def test_abstract_str():
    statement = LogicalOperator()
    str(statement)


@raises(NotImplementedError)
def test_abstract_repr():
    statement = LogicalOperator()
    repr(statement)


@raises(TypeError)
def test_invalid_statementicate():
    LogicalOperator("a")


def test_symbol():
    statement = Symbol('a')
    assert_equal(statement.arity, 0)
    assert_equal(repr(statement), "a")
    assert_equal(str(statement), "a")
    assert_is_not_none(hash(statement))


def test_not():
    statement_a = Symbol('a')
    statement_not = Not(statement_a)
    assert_equal(statement_not.arity, 1)
    assert_equal(repr(statement_not), "not(a)")
    assert_equal(str(statement_not), "~a")
    assert_is_not_none(hash(statement_not))


def test_and():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_and = And(statement_a, statement_b)
    assert_equal(statement_and.arity, 2)
    assert_equal(repr(statement_and), "and(a, b)")
    assert_equal(str(statement_and), "(a & b)")
    assert_is_not_none(hash(statement_and))


def test_or():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_or = Or(statement_a, statement_b)
    assert_equal(statement_or.arity, 2)
    assert_equal(repr(statement_or), "or(a, b)")
    assert_equal(str(statement_or), "(a | b)")
    assert_is_not_none(hash(statement_or))


def test_if():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_if = If(statement_a, statement_b)
    assert_equal(statement_if.arity, 2)
    assert_equal(repr(statement_if), "if(a, b)")
    assert_equal(str(statement_if), "(a -> b)")
    assert_is_not_none(hash(statement_if))


def test_iff():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_iff = Iff(statement_a, statement_b)
    assert_equal(statement_iff.arity, 2)
    assert_equal(repr(statement_iff), "iff(a, b)")
    assert_equal(str(statement_iff), "(a <-> b)")
    assert_is_not_none(hash(statement_iff))


def test_complex():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_and = And(statement_a, statement_b)
    statement_or = Or(statement_and, statement_a)
    statement_implies = If(statement_or, statement_and)
    statement_equiv = Iff(statement_implies, statement_a)
    assert_equal(repr(statement_equiv), "iff(if(or(and(a, b), a), "
                                        "and(a, b)), a)")
    assert_equal(str(statement_equiv), "((((a & b) | a) -> (a & b)) <-> a)")


def test_equality():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_and = And(statement_a, statement_b)
    statement_or = Or(statement_and, statement_a)
    statement_if = If(statement_or, statement_and)
    statement_iff = Iff(statement_if, statement_a)
    expected = Iff(If(Or(And(Symbol("a"), Symbol("b")), Symbol("a")),
                      And(Symbol("a"), Symbol("b"))), Symbol("a"))
    assert_true(expected == statement_iff)
    assert_equal(repr(expected), repr(statement_iff))
    assert_equal(str(expected), str(statement_iff))


def test_non_equality():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_and = And(statement_a, statement_b)
    statement_or = Or(statement_and, statement_b)
    assert_not_equal(statement_or, Or(And(Symbol('a'), Symbol('b')), Symbol('a')))


def test_non_equality_2():
    statement_1 = Not(Symbol("b"))
    statement_2 = Symbol("a")
    assert_not_equal(statement_1, statement_2)


def test_non_equality_symbol():
    assert_not_equal(Symbol("a"), Symbol("b"))


def test_non_equality_symbol_string():
    assert_not_equal(Symbol("a"), "a")


def test_equality_false_symbol_type():
    assert_false(Symbol("a") == "a")


@raises(TypeError)
def test_bad_symbol():
    Symbol(Symbol('a'))


def test_symbol_lt_symbol_1():
    assert_less(Symbol('a'), Symbol('b'))


def test_symbol_lt_operator_1():
    assert_less(Symbol('a'), Not(Symbol('a')))


def test_symbol_le_symbol():
    assert_less_equal(Symbol('a'), Symbol('b'))


def test_symbol_gt_symbol():
    assert_greater(Symbol('b'), Symbol('a'))


def test_symbol_ge_operator_1():
    assert_greater_equal(Symbol('b'), Symbol('a'))


def test_operator_not_lt_symbol():
    assert_false(Not(Symbol("a")) < Symbol("b"))


def test_operator_le_symbol():
    assert_less_equal(Not(Symbol('a')), Not(Symbol('b')))


def test_operator_gt_symbol():
    assert_greater(Not(Symbol("a")), Symbol("b"))


def test_operator_ge_symbol():
    assert_greater_equal(Not(Symbol("a")), Not(Symbol("a")))

if __name__ == "__main__":
    runmodule()