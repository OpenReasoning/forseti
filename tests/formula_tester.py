# pylint: disable=missing-docstring
"""
Tests to ensure that LogicalOperator representation works as expected
"""

from nose.tools import raises, assert_equal, assert_true, assert_not_equal, \
    assert_false, assert_less, assert_greater, assert_greater_equal
from forseti.formula import Symbol, LogicalOperator, Not, And, Or, Implies, \
    Equiv


@raises(NotImplementedError)
def test_abstract_get_print():
    statement = LogicalOperator()
    statement.get_print()


@raises(NotImplementedError)
def test_abstract_get_pretty_print():
    statement = LogicalOperator()
    statement.get_pretty_print()


@raises(NotImplementedError)
def test_abstract_print():
    statement = LogicalOperator()
    str(statement)


@raises(TypeError)
def test_invalid_statementicate():
    LogicalOperator("a")


def test_symbol():
    statement = Symbol('a')
    assert_equal(statement.arity, 0)
    assert_equal(statement.get_print(), "a")
    assert_equal(statement.get_pretty_print(), "a")


def test_not():
    statement_a = Symbol('a')
    statement_not = Not(statement_a)
    assert statement_not.arity == 1
    assert statement_not.get_print() == "not(a)"
    assert statement_not.get_pretty_print() == "~a"


def test_and():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_and = And(statement_a, statement_b)
    assert statement_and.arity == 2
    assert statement_and.get_print() == "and(a, b)"
    assert statement_and.get_pretty_print() == "(a & b)"


def test_or():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_or = Or(statement_a, statement_b)
    assert statement_or.arity == 2
    assert statement_or.get_print() == "or(a, b)", statement_or.get_print()
    assert statement_or.get_pretty_print() == "(a | b)"


def test_implies():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_implies = Implies(statement_a, statement_b)
    assert statement_implies.arity == 2
    assert_equal(statement_implies.get_print(), "implies(a, b)")
    assert_equal(statement_implies.get_pretty_print(), "(a -> b)")


def test_equiv():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_equiv = Equiv(statement_a, statement_b)
    assert statement_equiv.arity == 2
    assert statement_equiv.get_print() == "equiv(a, b)"
    assert statement_equiv.get_pretty_print() == "(a <-> b)"


def test_complex():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_and = And(statement_a, statement_b)
    statement_or = Or(statement_and, statement_a)
    statement_implies = Implies(statement_or, statement_and)
    statement_equiv = Equiv(statement_implies, statement_a)
    assert statement_equiv.get_print() == "equiv(implies(or(and(a, b), a), " \
                                          "and(a, b)), a)"
    assert statement_equiv.get_pretty_print() == "((((a & b) | a) -> (a & b))" \
                                                 " <-> a)"


def test_equality():
    statement_a = Symbol('a')
    statement_b = Symbol('b')
    statement_and = And(statement_a, statement_b)
    statement_or = Or(statement_and, statement_a)
    statement_implies = Implies(statement_or, statement_and)
    statement_equiv = Equiv(statement_implies, statement_a)
    expected = Equiv(Implies(Or(And(Symbol("a"), Symbol("b")), Symbol("a")),
                             And(Symbol("a"), Symbol("b"))), Symbol("a"))
    assert_true(expected == statement_equiv)
    assert_equal(expected.get_print(), statement_equiv.get_print())
    assert_equal(expected.get_pretty_print(),
                 statement_equiv.get_pretty_print())


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


def test_operator_not_lt_symbol():
    assert_false(Not(Symbol("a")) < Symbol("b"))


def test_operator_gt_symbol():
    assert_greater(Not(Symbol("a")), Symbol("b"))


def test_operator_ge_symbol():
    assert_greater_equal(Not(Symbol("a")), Not(Symbol("a")))
