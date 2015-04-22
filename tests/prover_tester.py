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


def test_prop_logic_1_1_1():
    prover = Prover()
    prover.add_formula(parser.parse("if(A,and(B,C))"))
    prover.add_formula(parser.parse("iff(C,B)"))
    prover.add_formula(parser.parse("not(C)"))
    prover.add_goal(parser.parse("not(A)"))
    assert_true(prover.run_prover())


def test_prop_logic_1_1_2():
    prover = Prover()
    prover.add_formula(parser.parse("if(K,H)"))
    prover.add_formula(parser.parse("if(H,L)"))
    prover.add_formula(parser.parse("if(L,M)"))
    prover.add_goal(parser.parse("if(K,M)"))
    assert_true(prover.run_prover())


def test_prob_logic_1_1_3():
    prover = Prover()
    prover.add_formula(parser.parse("not(iff(A,B))"))
    prover.add_formula(parser.parse("not(A)"))
    prover.add_formula(parser.parse("not(B)"))
    prover.add_goal(parser.parse("and(C,not(C))"))
    assert_true(prover.run_prover())


def test_prob_logic_1_1_4():
    prover = Prover()
    prover.add_formula(parser.parse("and(A,or(B,C))"))
    prover.add_formula(parser.parse("if(or(not(C),H),if(H,not(H)))"))
    prover.add_goal(parser.parse("and(A,B)"))
    assert_false(prover.run_prover())


def test_prob_logic_1_1_5():
    prover = Prover()
    prover.add_formula(parser.parse("if(R,Q)"))
    prover.add_formula(parser.parse("not(and(T,not(S)))"))
    prover.add_formula(parser.parse("or(not(Q),not(S))"))
    prover.add_goal(parser.parse("or(not(R),not(T))"))
    assert_true(prover.run_prover())


def test_prob_logic_1_1_6():
    prover = Prover()
    prover.add_formula(parser.parse("and(A,if(B,C))"))
    prover.add_goal(parser.parse("or(and(A,B),and(A,C))"))
    assert_false(prover.run_prover())


def test_prob_logic_1_1_7():
    prover = Prover()
    prover.add_formula(parser.parse("if(and(or(C,D),H),A)"))
    prover.add_formula(parser.parse("D"))
    prover.add_goal(parser.parse("if(H,A)"))
    assert_true(prover.run_prover())


def test_prob_logic_1_1_8():
    prover = Prover()
    prover.add_formula(parser.parse("if(or(J,M),not(and(J,M)))"))
    prover.add_formula(parser.parse("iff(M,if(M,J))"))
    prover.add_goal(parser.parse("if(M,J)"))
    assert_true(prover.run_prover())


def test_prop_logic_2_1_1():
    prover = Prover()
    prover.add_formula(parser.parse("and(R, and(C, not(F)))"))
    prover.add_formula(parser.parse("if(or(R,S),not(W))"))
    prover.add_goal(parser.parse("not(W)"))
    assert_true(prover.run_prover())


def test_prop_logic_2_1_2():
    prover = Prover()
    prover.add_formula(parser.parse("if(A,and(B,C))"))
    prover.add_formula(parser.parse("not(C)"))
    prover.add_goal(parser.parse("not(and(A, D))"))
    assert_true(prover.run_prover())


def test_prop_logic_2_1_3():
    prover = Prover()
    prover.add_formula(parser.parse("iff(A,B)"))
    prover.add_formula(parser.parse("iff(B,C)"))
    prover.add_goal(parser.parse("iff(A,C)"))
    assert_true(prover.run_prover())


def test_prop_logic_1_4():
    prover = Prover()
    prover.add_formula(parser.parse("iff(F,G)"))
    prover.add_formula(parser.parse("or(F, G)"))
    prover.add_goal(parser.parse("and(F, G)"))
    assert_true(prover.run_prover())


def test_prover_invalid():
    prover = Prover()
    prover.add_formula(parser.parse("not(iff(A, B))"))
    prover.add_goal(parser.parse("iff(not(A), not(B))"))
    assert_false(prover.run_prover())


@raises(TypeError)
def test_prover_formula_error():
    prover = Prover()
    prover.add_formula(None)


@raises(Exception)
def test_prover_no_goal_error():
    prover = Prover()
    prover.run_prover()
