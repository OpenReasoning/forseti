# pylint: disable=missing-docstring

from forseti.formula import Symbol, Not, And, Or, Iff
from forseti import converter, parser
from nose.tools import assert_equal, raises


def test_cnf_converter_symbol():
    statement = Symbol("a")
    statement = converter.convert_to_cnf(statement)
    expected = Symbol("a")
    assert_equal(expected, statement)


def test_cnf_converter_equiv():
    statement = Iff(Symbol("a"), Symbol("b"))
    statement = converter.convert_to_cnf(statement)
    expected = And(Or(Not(Symbol("a")), Symbol("b")),
                   Or(Not(Symbol("b")), Symbol("a")))
    assert_equal(expected, statement)


def test_cnf_not_distribution():
    statement = Not(And(Symbol("a"), Symbol("b")))
    statement = converter.convert_to_cnf(statement)
    expected = Or(Not(Symbol("a")), Not(Symbol("b")))
    assert_equal(expected, statement)


def test_cnf_not_distribution_2():
    statement = Not(Or(And(Symbol("a"), Not(Symbol("b"))), Not(Symbol("c"))))
    statement = converter.convert_to_cnf(statement)
    expected = And(Or(Not(Symbol("a")), Symbol("b")), Symbol("c"))
    assert_equal(expected, statement)


def test_cnf_or_distribution():
    statement = Or(And(Symbol("a"), Symbol("b")), Symbol("c"))
    statement = converter.convert_to_cnf(statement)
    expected = And(Or(Symbol("a"), Symbol("c")), Or(Symbol("b"), Symbol("c")))
    assert_equal(expected, statement)


def test_cnf_negation():
    statement = Not(Not(And(Symbol("a"), Symbol("b"))))
    statement = converter.convert_to_cnf(statement)
    expected = And(Symbol("a"), Symbol("b"))
    assert_equal(expected, statement)


def test_convert_to_cnf():
    statement = Not(Iff(Symbol("a"), Symbol("c")))
    statement = converter.convert_to_cnf(statement)
    a_symbol = Symbol("a")
    c_symbol = Symbol("c")
    expected = And(And(Or(c_symbol, a_symbol), Or(Not(a_symbol), a_symbol)),
                   And(Or(c_symbol, Not(c_symbol)), Or(Not(a_symbol),
                                                       Not(c_symbol))))
    assert_equal(expected, statement)


def test_convert_to_cnf_2():
    statement = parser.parse("forall(x,if(A(x),and(B(x),C(x))))")
    statement = converter.convert_to_cnf(statement)
    expected = "((B(Herbrand1) | ~A(Herbrand1)) & (C(Herbrand1) | ~A(Herbrand1)))"
    assert_equal(expected, str(statement))


@raises(TypeError)
def test_cnf_error_on_string():
    converter.convert_to_cnf("invalid")
