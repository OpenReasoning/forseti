"""
Tester for Forseti prover engine for Propositional Calculus (PC)

All test cases taken from handouts provided by Dr. Bram van Heuveln
as part of Compubility & Logic. Naming scheme is
x_y_z
x = which batch of propositional logic arguments question came from
y = which handout in the batch
z = which problem in the handout

Batch 1 contained some valid, some invalid
Batch 2 contained only valid
"""

# pylint: disable=missing-docstring

from forseti.prover import Prover
from nose.tools import assert_false, assert_true


def test_prop_logic_1_1_1():
    prover = Prover()
    prover.add_formula("if(A,and(B,C))")
    prover.add_formula("iff(C,B)")
    prover.add_formula("not(C)")
    prover.add_goal("not(A)")
    assert_true(prover.run_prover())


def test_prop_logic_1_1_2():
    prover = Prover()
    prover.add_formula("if(K,H)")
    prover.add_formula("if(H,L)")
    prover.add_formula("if(L,M)")
    prover.add_goal("if(K,M)")
    assert_true(prover.run_prover())


def test_prob_logic_1_1_3():
    prover = Prover()
    prover.add_formula("not(iff(A,B))")
    prover.add_formula("not(A)")
    prover.add_formula("not(B)")
    prover.add_goal("and(C,not(C))")
    assert_true(prover.run_prover())


def test_prob_logic_1_1_4():
    prover = Prover()
    prover.add_formula("and(A,or(B,C))")
    prover.add_formula("if(or(not(C),H),if(H,not(H)))")
    prover.add_goal("and(A,B)")
    assert_false(prover.run_prover())


def test_prob_logic_1_1_5():
    prover = Prover()
    prover.add_formula("if(R,Q)")
    prover.add_formula("not(and(T,not(S)))")
    prover.add_formula("or(not(Q),not(S))")
    prover.add_goal("or(not(R),not(T))")
    assert_true(prover.run_prover())


def test_prob_logic_1_1_6():
    prover = Prover()
    prover.add_formula("and(A,if(B,C))")
    prover.add_goal("or(and(A,B),and(A,C))")
    assert_false(prover.run_prover())


def test_prob_logic_1_1_7():
    prover = Prover()
    prover.add_formula("if(and(or(C,D),H),A)")
    prover.add_formula("D")
    prover.add_goal("if(H,A)")
    assert_true(prover.run_prover())


def test_prob_logic_1_1_8():
    prover = Prover()
    prover.add_formula("if(or(J,M),not(and(J,M)))")
    prover.add_formula("iff(M,if(M,J))")
    prover.add_goal("if(M,J)")
    assert_true(prover.run_prover())


def test_prob_logic_1_1_9():
    prover = Prover()
    prover.add_formula("not(iff(A,B))")
    prover.add_goal("iff(not(A),not(B))")
    assert_false(prover.run_prover())


def test_prob_logic_1_1_10():
    prover = Prover()
    prover.add_goal("iff(if(not(P),P),P)")
    assert_false(prover.run_prover())


def test_prob_logic_1_1_11():
    prover = Prover()
    prover.add_formula("if(M,if(K,B))")
    prover.add_formula("if(not(K),not(M))")
    prover.add_formula("and(L,M)")
    prover.add_goal("B")
    assert_true(prover.run_prover())


def test_prob_logic_1_1_12():
    prover = Prover()
    prover.add_formula("if(or(not(J),K),and(L,M))")
    prover.add_formula("not(or(not(J),K))")
    prover.add_goal("not(and(L,M))")
    assert_false(prover.run_prover())


def test_prob_logic_1_1_13():
    prover = Prover()
    prover.add_formula("not(and(not(A),not(B)))")
    prover.add_goal("and(A,B)")
    assert_false(prover.run_prover())


def test_prob_logic_1_1_14():
    prover = Prover()
    prover.add_formula("or(iff(M,K),not(and(K,D)))")
    prover.add_formula("if(not(M),not(K))")
    prover.add_formula("if(not(D),not(and(K,D)))")
    prover.add_goal("M")
    assert_false(prover.run_prover())


def test_prob_logic_1_1_15():
    prover = Prover()
    prover.add_formula("and(B,or(H,Z))")
    prover.add_formula("if(not(Z),K)")
    prover.add_formula("if(iff(B,Z),not(Z))")
    prover.add_formula("not(K)")
    prover.add_goal("and(M,N)")
    assert_true(prover.run_prover())


def test_prob_logic_1_1_16():
    prover = Prover()
    prover.add_formula("and(iff(D,not(G)),G)")
    prover.add_formula("if(or(G,and(if(A,D),A)),not(D))")
    prover.add_goal("if(G,not(D))")
    assert_true(prover.run_prover())


def test_prob_logic_1_1_17():
    prover = Prover()
    prover.add_formula("if(J,if(T,J))")
    prover.add_formula("if(T,if(J,T))")
    prover.add_goal("and(not(J),not(T))")
    assert_false(prover.run_prover())


def test_prob_logic_1_1_18():
    prover = Prover()
    prover.add_formula("and(A,if(B,C))")
    prover.add_goal("or(and(A,C),and(A,not(B)))")
    assert_true(prover.run_prover())


def test_prob_logic_1_1_19():
    prover = Prover()
    prover.add_formula("or(A,not(and(B,C)))")
    prover.add_formula("not(B)")
    prover.add_formula("not(or(A,C))")
    prover.add_formula("not(or(A,C))")
    prover.add_goal("A")
    assert_false(prover.run_prover())


def test_prop_logic_1_1_20():
    prover = Prover()
    prover.add_formula("or(iff(G,H),iff(not(G),H))")
    prover.add_goal("or(iff(not(G),not(H)),not(iff(G,H)))")
    assert_true(prover.run_prover())


def test_prop_logic_2_1_1():
    prover = Prover()
    prover.add_formula("and(R, and(C, not(F)))")
    prover.add_formula("if(or(R,S),not(W))")
    prover.add_goal("not(W)")
    assert_true(prover.run_prover())


def test_prop_logic_2_1_2():
    prover = Prover()
    prover.add_formula("if(A,and(B,C))")
    prover.add_formula("not(C)")
    prover.add_goal("not(and(A, D))")
    assert_true(prover.run_prover())


def test_prop_logic_2_1_3():
    prover = Prover()
    prover.add_formula("iff(A,B)")
    prover.add_formula("iff(B,C)")
    prover.add_goal("iff(A,C)")
    assert_true(prover.run_prover())


def test_prop_logic_1_4():
    prover = Prover()
    prover.add_formula("iff(F,G)")
    prover.add_formula("or(F, G)")
    prover.add_goal("and(F, G)")
    assert_true(prover.run_prover())


def test_prover_invalid():
    prover = Prover()
    prover.add_formula("not(iff(A, B))")
    prover.add_goal("iff(not(A), not(B))")
    assert_false(prover.run_prover())
