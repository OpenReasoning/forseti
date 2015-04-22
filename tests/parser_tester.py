# pylint: disable=missing-docstring

from forseti import parser
from forseti.formula import Symbol, Not, And, Or, If, Iff
from nose.tools import assert_equal, raises


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
