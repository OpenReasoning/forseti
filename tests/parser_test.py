# pylint: disable=missing-docstring

from forseti import parser
from forseti.predicate import Atomic, Not, And, Or, Implies, Equiv


def test_empty_parse():
    pred = parser.parse("")
    assert pred is None


def test_parse_atomic():
    pred = parser.parse("a")
    assert pred == Atomic("a")


def test_parse_not():
    pred = parser.parse("not(a)")
    assert pred == Not(Atomic("a"))


def test_parse_and():
    pred = parser.parse("and(a, b)")
    assert pred == And(Atomic("a"), Atomic("b"))


def test_parse_or():
    pred = parser.parse("or(a, b)")
    assert pred == Or(Atomic("a"), Atomic("b"))


def test_parse_implies():
    pred = parser.parse("implies(a, b)")
    assert pred == Implies(Atomic("a"), Atomic("b"))


def test_parse_equiv():
    pred = parser.parse("equiv(a, b)")
    assert pred == Equiv(Atomic("a"), Atomic("b"))


def test_bad_atomic():
    pred = parser.parse("&a")
    assert pred is None


def test_extra_paranthesis():
    pred = parser.parse("and((a),((b)))")
    assert pred == And(Atomic("a"), Atomic("b"))


def test_bad_paranthesis():
    pred = parser.parse("and((a)),b)")
    assert pred is None
