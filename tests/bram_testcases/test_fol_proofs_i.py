import unittest
from forseti.prover import Prover
from forseti.formula import Predicate, Skolem, Herbrand


class TestFOLProofsI(unittest.TestCase):
    def setUp(self):
        Predicate.reset()
        Skolem.reset()
        Herbrand.reset()

    def test_problem_01(self):
        prover = Prover()
        prover.add_formula("forall(x,if(A(x),B(x)))")
        prover.add_formula("forall(x,if(B(x),C(x)))")
        prover.add_goal("forall(x,if(A(x),C(x)))")
        self.assertTrue(prover.run_prover())

    def test_problem_02(self):
        prover = Prover()
        prover.add_formula("forall(x,if(A(x),and(B(x),C(x))))")
        prover.add_formula("forall(x,if(A(x),not(C(x))))")
        prover.add_goal("not(A(a))")
        self.assertTrue(prover.run_prover())

    def test_problem_03(self):
        prover = Prover()
        prover.add_formula("forall(x,if(A(x),B(x)))")
        prover.add_formula("forall(x,if(not(A(x)),C(x)))")
        prover.add_goal("forall(x,if(not(B(x)),not(C(x))))")
        self.assertFalse(prover.run_prover())

    def test_problem_04(self):
        prover = Prover()
        prover.add_formula("exists(x,and(A(x),not(B(x))))")
        prover.add_formula("exists(x,and(A(x),not(C(x))))")
        prover.add_formula("exists(x,and(not(B(x)),D(x)))")
        prover.add_goal("exists(x,and(and(A(x),not(B(x))),D(x)))")
        self.assertFalse(prover.run_prover())

    def test_problem_05(self):
        prover = Prover()
        prover.add_formula("forall(x,if(A(x),F(x)))")
        prover.add_formula("if(exists(x,F(x)),not(exists(y,G(y))))")
        prover.add_goal("forall(x,if(exists(y,A(y)),not(G(x))))")
        self.assertTrue(prover.run_prover())

    def test_problem_06(self):
        prover = Prover()
        prover.add_formula("exists(x,or(A(x),not(B(x))))")
        prover.add_formula("forall(x,if(and(A(x),not(B(x))),C(x)))")
        prover.add_goal("exists(x,C(x))")
        self.assertFalse(prover.run_prover())

    def test_problem_07(self):
        prover = Prover()
        prover.add_formula("forall(x,not(F(x,x)))")
        prover.add_formula("if(not(forall(x,G(x))),exists(y,F(y,a)))")
        prover.add_goal("exists(z,and(G(z),F(z,z)))")
        self.assertFalse(prover.run_prover())

    def test_problem_08(self):
        prover = Prover()
        prover.add_formula("forall(x,exists(y,and(F(x),G(x,y))))")
        prover.add_goal("exists(y,forall(x,and(F(x),G(x,y))))")
        self.assertFalse(prover.run_prover())

    def test_problem_09(self):
        prover = Prover()
        prover.add_formula("exists(x,and(F(x),forall(y,if(G(y),L(x,y)))))")
        prover.add_formula("forall(x,if(F(x),forall(y,if(M(y),not(L(x,y))))))")
        prover.add_goal("forall(x,if(G(x),not(M(x))))")
        self.assertTrue(prover.run_prover())

    def test_problem_10(self):
        prover = Prover()
        prover.add_formula("or(F(a),exists(y,G(y,a)))")
        prover.add_formula("or(F(b),exists(y,not(G(y,a))))")
        prover.add_goal("exists(y,G(y,a))")
        self.assertFalse(prover.run_prover())

    def test_problem_11(self):
        prover = Prover()
        prover.add_formula("forall(x,not(J(x)))")
        prover.add_formula("if(exists(y,or(H(b,y),R(y,y))),exists(x,J(x)))")
        prover.add_goal("forall(y,not(or(H(b,y),R(y,y))))")
        self.assertTrue(prover.run_prover())

    def test_problem_12(self):
        prover = Prover()
        prover.add_formula("forall(z,iff(L(z),H(z)))")
        prover.add_formula("forall(x,not(or(H(x),not(B(x)))))")
        prover.add_goal("not(L(b))")
        self.assertTrue(prover.run_prover())

    def test_problem_13(self):
        prover = Prover()
        prover.add_formula("or(not(forall(x,K(x,x))),forall(y,H(y,y)))")
        prover.add_goal("exists(z,if(not(H(z,z)),not(K(z,z))))")
        self.assertTrue(prover.run_prover())

    def test_problem_14(self):
        prover = Prover()
        prover.add_formula("forall(x,forall(y,or(F(x),G(x,y))))")
        prover.add_formula("exists(x,F(x))")
        prover.add_goal("exists(x,exists(y,G(x,y)))")
        self.assertFalse(prover.run_prover())

    def test_problem_15(self):
        prover = Prover()
        prover.add_formula("forall(x,forall(y,forall(z,if(and(L(x,y),L(y,z)),"
                           "L(x,z)))))")
        prover.add_formula("forall(x,forall(y,if(L(x,y),L(y,x))))")
        prover.add_goal("forall(x,L(x,x))")
        self.assertFalse(prover.run_prover())

    def test_problem_16(self):
        prover = Prover()
        prover.add_formula("forall(x,if(S(x),exists(y,and(S(y),forall(z,"
                           "iff(B(z,y),and(B(z,x),B(z,z))))))))")
        prover.add_formula("forall(x,not(B(x,x)))")
        prover.add_formula("exists(x,S(x))")
        prover.add_goal("exists(x,and(S(x),forall(y,not(B(y,x)))))")
        self.assertTrue(prover.run_prover())

    def test_problem_17(self):
        prover = Prover()
        prover.add_formula("forall(x,forall(y,if(and(A(x),B(y)),C(x,y))))")
        prover.add_formula("exists(y,and(F(y),forall(z,if(H(z),C(y,z)))))")
        prover.add_formula("forall(x,forall(y,forall(z,if(and(L(x,y),L(y,z)),"
                           "L(x,z)))))")
        prover.add_formula("forall(x,if(F(x),B(x)))")
        prover.add_goal("forall(z,forall(y,if(and(A(z),H(y)),C(z,y))))")
        self.assertFalse(prover.run_prover())

    def test_problem_18(self):
        self.skipTest('Should work')
        prover = Prover()
        prover.add_formula("forall(x,if(exists(y,and(A(y),B(x,y))),C(x)))")
        prover.add_formula("exists(y,and(D(y),exists(x,and(F(x),and(G(x),B(y,x))))))")
        prover.add_formula("forall(x,if(F(x),A(x)))")
        prover.add_formula(
            "if(exists(x,and(C(x),D(x))),if(exists(y,and(D(y),exists(z,B(y,z)))),forall(x,F(x))))")
        prover.add_goal("forall(x,A(x))")
        self.assertTrue(prover.run_prover())


if __name__ == '__main__':
    unittest.main()