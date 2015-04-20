"""
Tester for Forseti prover engine

All test cases taken from handouts provided by Dr. Bram van Heuveln
as part of Compubility & Logic. Naming scheme is
x_y_z
x = which batch of propositional logic arguments question came from
y = which handout in the batch
z = which problem in the handout

Batch 1 contained some valid, some invalid
Batch 2 contained only valid
"""

# pylint: disable=missing-docstring,unreachable

from forseti.prover import Prover
from forseti import parser
from nose.tools import assert_false, assert_true, raises
from nose.plugins.skip import SkipTest


def test_prop_logic_1_1_1():
    prover = Prover()
    prover.add_formula(parser.parse("implies(A,and(B,C))"))
    prover.add_formula(parser.parse("equiv(C,B)"))
    prover.add_formula(parser.parse("not(C)"))
    prover.add_goal(parser.parse("not(A)"))
    assert_true(prover.run_prover())


def test_prop_logic_1_1_2():
    prover = Prover()
    prover.add_formula(parser.parse("implies(K,H)"))
    prover.add_formula(parser.parse("implies(H,L)"))
    prover.add_formula(parser.parse("implies(L,M)"))
    prover.add_goal(parser.parse("implies(K,M)"))
    assert_true(prover.run_prover())


def test_prob_logic_1_1_3():
    prover = Prover()
    prover.add_formula(parser.parse("not(equiv(A,B))"))
    prover.add_formula(parser.parse("not(A)"))
    prover.add_formula(parser.parse("not(B)"))
    prover.add_goal(parser.parse("and(C,not(C))"))
    assert_true(prover.run_prover())


def test_prob_logic_1_1_4():
    prover = Prover()
    prover.add_formula(parser.parse("and(A,or(B,C))"))
    prover.add_formula(parser.parse("implies(or(not(C),H),implies(H,not(H)))"))
    prover.add_goal(parser.parse("and(A,B)"))
    assert_false(prover.run_prover())


def test_prob_logic_1_1_5():
    prover = Prover()
    prover.add_formula(parser.parse("implies(R,Q)"))
    prover.add_formula(parser.parse("not(and(T,not(S)))"))
    prover.add_formula(parser.parse("or(not(Q),not(S))"))
    prover.add_goal(parser.parse("or(not(R),not(T))"))
    assert_true(prover.run_prover())


def test_prob_logic_1_1_6():
    prover = Prover()
    prover.add_formula(parser.parse("and(A,implies(B,C))"))
    prover.add_goal(parser.parse("or(and(A,B),and(A,C))"))
    assert_false(prover.run_prover())


def test_prob_logic_1_1_7():
    prover = Prover()
    prover.add_formula(parser.parse("implies(and(or(C,D),H),A)"))
    prover.add_formula(parser.parse("D"))
    prover.add_goal(parser.parse("implies(H,A)"))
    assert_true(prover.run_prover())


def test_prob_logic_1_1_8():
    raise SkipTest
    prover = Prover()
    prover.add_formula(parser.parse("implies(or(J,M),not(and(J,M)))"))
    prover.add_formula(parser.parse("equiv(M,implies(M,J))"))
    prover.add_goal(parser.parse("implies(M,J)"))
    assert_true(prover.run_prover())


def test_shell():
    raise SkipTest
    prover = Prover()
    assert_true(prover.run_prover())


def test_prop_logic_2_1_1():
    prover = Prover()
    prover.add_formula(parser.parse("and(R, and(C, not(F)))"))
    prover.add_formula(parser.parse("implies(or(R,S),not(W))"))
    prover.add_goal(parser.parse("not(W)"))
    assert_true(prover.run_prover())


def test_prop_logic_2_1_2():
    prover = Prover()
    prover.add_formula(parser.parse("implies(A,and(B,C))"))
    prover.add_formula(parser.parse("not(C)"))
    prover.add_goal(parser.parse("not(and(A, D))"))
    assert_true(prover.run_prover())


def test_prop_logic_2_1_3():
    raise SkipTest
    prover = Prover()
    prover.add_formula(parser.parse("equiv(A,B)"))
    prover.add_formula(parser.parse("equiv(B,C)"))
    prover.add_goal(parser.parse("equiv(A,C)"))
    assert_true(prover.run_prover())


def test_prop_logic_1_4():
    raise SkipTest
    prover = Prover()
    prover.add_formula(parser.parse("equiv(F,G)"))
    prover.add_formula(parser.parse("or(F, G)"))
    prover.add_goal(parser.parse("and(F, G)"))
    assert_true(prover.run_prover())


def test_prover_invalid():
    prover = Prover()
    prover.add_formula(parser.parse("not(equiv(A, B))"))
    prover.add_goal(parser.parse("equiv(not(A), not(B))"))
    assert_false(prover.run_prover())


@raises(TypeError)
def test_prover_formula_error():
    prover = Prover()
    prover.add_formula(None)


@raises(Exception)
def test_prover_no_goal_error():
    prover = Prover()
    prover.run_prover()
