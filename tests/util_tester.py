# pylint: disable=missing-docstring
from six import StringIO
from forseti.formula import Symbol, Not
import forseti.util as util
from nose.tools import assert_equal, assert_true, assert_false


def test_print_cnf_list():
    cnf = list()
    a_symbol = Symbol("a")
    b_symbol = Symbol("b")
    not_a = Not(a_symbol)
    not_b = Not(b_symbol)
    cnf.append([a_symbol, b_symbol])
    cnf.append([not_b, a_symbol])
    cnf.append([not_a, not_b])
    writer = StringIO()
    util.print_cnf_list(cnf, out=writer)
    cnf_list = "[[a, b], [not(b), a], [not(a), not(b)]]\n"
    assert_equal(cnf_list, writer.getvalue())


def test_negate_symbol():
    negate = util.negate_formula(Symbol("a"))
    assert_equal(Not(Symbol("a")), negate)


def test_negate_not():
    negate = util.negate_formula(Not(Symbol("a")))
    assert_equal(Symbol("a"), negate)


def test_is_tautology():
    cnf = list()
    cnf.append(Symbol("a"))
    cnf.append(Not(Symbol("a")))
    is_taut = util.is_tautology(cnf)
    assert_true(is_taut)


def test_is_tautology_negative():
    cnf = list()
    cnf.append(Symbol("a"))
    cnf.append(Symbol("b"))
    is_taut = util.is_tautology(cnf)
    assert_false(is_taut)


def test_is_tautology_bad_input():
    assert_false(util.is_tautology("a"))
    assert_false(util.is_tautology([Symbol("a")]))
