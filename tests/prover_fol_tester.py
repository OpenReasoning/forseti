# pylint: disable=missing-docstring

from nose.tools import assert_false, assert_true, with_setup
from forseti.prover import Prover
from forseti.formula import Predicate, Herbrand, Skolem
from nose.plugins.skip import SkipTest

def setup():
    Predicate.reset()
    Herbrand.reset()
    Skolem.reset()

# 26 tests


@with_setup(setup)
def test_fol_logic_1_1():
    prover = Prover()
    prover.add_formula("forall(x,if(A(x),B(x)))")
    prover.add_formula("forall(x,if(B(x),C(x)))")
    prover.add_goal("forall(x,if(A(x),C(x)))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_2():
    prover = Prover()
    prover.add_formula("forall(x,if(A(x),and(B(x),C(x))))")
    prover.add_formula("forall(x,if(A(x),not(C(x))))")
    prover.add_goal("not(A(a))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_3():
    prover = Prover()
    prover.add_formula("forall(x,if(A(x),B(x)))")
    prover.add_formula("forall(x,if(not(A(x)),C(x)))")
    prover.add_goal("forall(x,if(not(B(x)),not(C(x))))")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_4():
    prover = Prover()
    prover.add_formula("exists(x,and(A(x),not(B(x))))")
    prover.add_formula("exists(x,and(A(x),not(C(x))))")
    prover.add_formula("exists(x,and(not(B(x)),D(x)))")
    prover.add_goal("exists(x,and(and(A(x),not(B(x))),D(x)))")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_5():
    prover = Prover()
    prover.add_formula("forall(x,if(A(x),F(x)))")
    prover.add_formula("if(exists(x,F(x)),not(exists(y,G(y))))")
    prover.add_goal("forall(x,if(exists(y,A(y)),not(G(x))))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_6():
    prover = Prover()
    prover.add_formula("exists(x,or(A(x),not(B(x))))")
    prover.add_formula("forall(x,if(and(A(x),not(B(x))),C(x)))")
    prover.add_goal("exists(x,C(x))")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_7():
    prover = Prover()
    prover.add_formula("forall(x,not(F(x,x)))")
    prover.add_formula("if(not(forall(x,G(x))),exists(y,F(y,a)))")
    prover.add_goal("exists(z,and(G(z),F(z,z)))")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_8():
    prover = Prover()
    prover.add_formula("forall(x,exists(y,and(F(x),G(x,y))))")
    prover.add_goal("exists(y,forall(x,and(F(x),G(x,y))))")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_9():
    prover = Prover()
    prover.add_formula("exists(x,and(F(x),forall(y,if(G(y),L(x,y)))))")
    prover.add_formula("forall(x,if(F(x),forall(y,if(M(y),not(L(x,y))))))")
    prover.add_goal("forall(x,if(G(x),not(M(x))))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_10():
    prover = Prover()
    prover.add_formula("or(F(a),exists(y,G(y,a)))")
    prover.add_formula("or(F(b),exists(y,not(G(y,a))))")
    prover.add_goal("exists(y,G(y,a))")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_11():
    prover = Prover()
    prover.add_formula("forall(x,not(J(x)))")
    prover.add_formula("if(exists(y,or(H(b,y),R(y,y))),exists(x,J(x)))")
    prover.add_goal("forall(y,not(or(H(b,y),R(y,y))))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_12():
    prover = Prover()
    prover.add_formula("forall(z,iff(L(z),H(z)))")
    prover.add_formula("forall(x,not(or(H(x),not(B(x)))))")
    prover.add_goal("not(L(b))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_13():
    prover = Prover()
    prover.add_formula("or(not(forall(x,K(x,x))),forall(y,H(y,y)))")
    prover.add_goal("exists(z,if(not(H(z,z)),not(K(z,z))))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_14():
    prover = Prover()
    prover.add_formula("forall(x,forall(y,or(F(x),G(x,y))))")
    prover.add_formula("exists(x,F(x))")
    prover.add_goal("exists(x,exists(y,G(x,y)))")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_15():
    prover = Prover()
    prover.add_formula("forall(x,forall(y,forall(z,if(and(L(x,y),L(y,z)),"
                       "L(x,z)))))")
    prover.add_formula("forall(x,forall(y,if(L(x,y),L(y,x))))")
    prover.add_goal("forall(x,L(x,x))")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_16():
    prover = Prover()
    prover.add_formula("forall(x,if(S(x),exists(y,and(S(y),forall(z,"
                       "iff(B(z,y),and(B(z,x),B(z,z))))))))")
    prover.add_formula("forall(x,not(B(x,x)))")
    prover.add_formula("exists(x,S(x))")
    prover.add_goal("exists(x,and(S(x),forall(y,not(B(y,x)))))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_1_17():
    prover = Prover()
    prover.add_formula("forall(x,forall(y,if(and(A(x),B(y)),C(x,y))))")
    prover.add_formula("exists(y,and(F(y),forall(z,if(H(z),C(y,z)))))")
    prover.add_formula("forall(x,forall(y,forall(z,if(and(L(x,y),L(y,z)),"
                       "L(x,z)))))")
    prover.add_formula("forall(x,if(F(x),B(x)))")
    prover.add_goal("forall(z,forall(y,if(and(A(z),H(y)),C(z,y))))")
    assert_false(prover.run_prover())


@SkipTest
@with_setup(setup)
def test_fol_logic_1_18():
    prover = Prover()
    prover.add_formula("forall(x,if(exists(y,and(A(y),B(x,y))),C(x)))")
    prover.add_formula("exists(y,and(D(y),exists(x,and(F(x),and(G(x),B(y,x))))))")
    prover.add_formula("forall(x,if(F(x),A(x)))")
    prover.add_formula("if(exists(x,and(C(x),D(x))),if(exists(y,and(D(y),exists(z,B(y,z)))),forall(x,F(x))))")
    prover.add_goal("forall(x,A(x))")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_1():
    prover = Prover()
    prover.add_formula("forall(x,if(A(x),B(x)))")
    prover.add_formula("forall(x,if(B(x),C(x)))")
    prover.add_goal("forall(x,if(A(x),C(x)))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_2():
    prover = Prover()
    prover.add_formula("forall(x,if(A(x),and(B(x),C(x))))")
    prover.add_formula("forall(x,if(A(x),not(C(x))))")
    prover.add_goal("not(A(a))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_3():
    prover = Prover()
    prover.add_formula("forall(x,if(A(x),forall(y,B(x,y))))")
    prover.add_formula("A(b)")
    prover.add_goal("forall(y,B(b,y))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_4():
    prover = Prover()
    prover.add_formula("forall(x,if(B(x),C(x)))")
    prover.add_formula("exists(y,and(A(y),B(y)))")
    prover.add_goal("exists(z,and(A(z),C(z)))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_5():
    prover = Prover()
    prover.add_formula("not(exists(z,F(z)))")
    prover.add_goal("if(F(a),G(a))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_6():
    prover = Prover()
    prover.add_formula("exists(x,if(A(x),forall(x,if(B(x),C(x)))))")
    prover.add_formula("and(A(c),B(c))")
    prover.add_goal("C(c)")
    assert_false(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_7():
    prover = Prover()
    prover.add_formula("forall(x,if(B(x),C(x)))")
    prover.add_formula("exists(y,not(C(y)))")
    prover.add_goal("exists(z,not(B(z)))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_8():
    prover = Prover()
    prover.add_formula("K(a)")
    prover.add_formula("forall(x,if(K(x),forall(y,H(y))))")
    prover.add_goal("forall(x,H(x))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_9():
    prover = Prover()
    prover.add_formula("forall(x,exists(y,if(A(x),B(y))))")
    prover.add_goal("forall(x,if(F(x),exists(y,B(y))))")
    assert_false(prover.run_prover())


@SkipTest
@with_setup(setup)
def test_fol_logic_2_10():
    prover = Prover()
    prover.add_formula("exists(x,forall(y,A(x,y)))")
    prover.add_goal("exists(x,A(x,a))")
    assert_true(prover.run_prover())


@with_setup(setup)
def test_fol_logic_2_11():
    prover = Prover()
    prover.add_formula("if(forall(x,A(x)),exists(y,B(y)))")
    prover.add_formula("forall(y,not(B(y)))")
    prover.add_goal("not(forall(z,A(z)))")
    assert_true(prover.run_prover())
