# pylint: disable=missing-docstring

from __future__ import unicode_literals
from forseti import parser
from forseti.formula import Symbol, Not, And, Or, If, Iff, Universal, \
    Predicate, Skolem, Herbrand
import nose
from nose.tools import assert_equal, raises, with_setup


def setup():
    Predicate.reset()
    Herbrand.reset()
    Skolem.reset()


def test_parse_symbol():
    statement = parser.parse("a")
    assert_equal(statement, Symbol("a"))


def test_parse_not():
    statement = parser.parse("not(a)")
    assert_equal(statement, Not(Symbol("a")))


def test_parse_and():
    statement = parser.parse("and(a, b)")
    assert_equal(statement, And(Symbol("a"), Symbol("b")))


def test_parse_or():
    statement = parser.parse("or(a, b)")
    assert_equal(statement, Or(Symbol("a"), Symbol("b")))


def test_parse_if():
    statement = parser.parse("if(a, b)")
    assert_equal(statement, If(Symbol("a"), Symbol("b")))


def test_parse_iff():
    statement = parser.parse("iff(a, b)")
    assert_equal(statement, Iff(Symbol("a"), Symbol("b")))


def test_parse_iff_2():
    statement = parser.parse("iff(not(A), not(B))")
    assert_equal(statement, Iff(Not(Symbol("A")), Not(Symbol("B"))))


def test_extra_paranthesis():
    statement = parser.parse("and((a),((b)))")
    assert_equal(And(Symbol("a"), Symbol("b")), statement)


@with_setup(setup)
def test_parse_fol_1():
    statement = parser.parse("forall(x,if(A(x),and(B(x),C(x))))")
    expected = Universal(Symbol("x"), If(Predicate("A", [Symbol("x")]),
                                         And(Predicate("B", [Symbol("x")]),
                                             Predicate("C", [Symbol("x")]))))

    assert_equal(expected, statement)


@raises(SyntaxError)
def test_empty_parse():
    parser.parse("")


@raises(SyntaxError)
def test_bad_symbol():
    parser.parse("&a")


@raises(SyntaxError)
def test_bad_paranthesis():
    parser.parse("and((a)),b)")


@raises(SyntaxError)
def test_bad_paranthesis_left():
    parser.parse("and(a,b")


@raises(SyntaxError)
def test_wrong_number_arguments():
    parser.parse("and(a)")


@raises(SyntaxError)
def test_invalid_formula():
    parser.parse("not(a),")


@raises(SyntaxError)
def test_extra_comma():
    parser.parse("and(a!,b)")

if __name__ == "__main__":
    nose.runmodule()