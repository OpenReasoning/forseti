import unittest
from forseti.prover import Prover


class TestPropLogicArgumentsII(unittest.TestCase):
    def test_problem_01(self):
        prover = Prover()
        prover.add_formula('if(K, not(K))')
        prover.add_goal('not(K)')
        self.assertTrue(prover.run_prover())

    def test_problem_02(self):
        prover = Prover()
        prover.add_formula('if(R, R)')
        prover.add_goal('R')
        self.assertFalse(prover.run_prover())

    def test_problem_03(self):
        prover = Prover()
        prover.add_formula('iff(P, not(N))')
        prover.add_goal('or(N, P)')
        self.assertTrue(prover.run_prover())

    def test_problem_04(self):
        prover = Prover()
        prover.add_formula('not(and(G, M))')
        prover.add_formula('or(M, not(G))')
        prover.add_goal('not(G)')
        self.assertTrue(prover.run_prover())

    def test_problem_05(self):
        prover = Prover()
        prover.add_formula('iff(K, not(L))')
        prover.add_formula('not(and(L, not(K)))')
        prover.add_goal('if(K, L)')
        self.assertFalse(prover.run_prover())

    def test_problem_06(self):
        prover = Prover()
        prover.add_formula('Z')
        prover.add_goal('if(E, if(Z, E))')
        self.assertTrue(prover.run_prover())

    def test_problem_07(self):
        prover = Prover()
        prover.add_formula('not(and(W, not(X)))')
        prover.add_formula('not(and(X, not(W)))')
        prover.add_goal('or(X, W)')
        self.assertFalse(prover.run_prover())

    def test_problem_08(self):
        prover = Prover()
        prover.add_formula('iff(C, D)')
        prover.add_formula('or(E, not(D))')
        prover.add_goal('if(E, C)')
        self.assertFalse(prover.run_prover())

    def test_problem_09(self):
        prover = Prover()
        prover.add_formula('iff(A, and(B, C))')
        prover.add_formula('or(not(C), B)')
        prover.add_goal('if(A, B)')
        self.assertTrue(prover.run_prover())

    def test_problem_10(self):
        prover = Prover()
        prover.add_formula('if(J, if(K, L))')
        prover.add_formula('if(K, if(J, L))')
        prover.add_goal('if(or(J, K), L)')
        self.assertFalse(prover.run_prover())

    def test_problem_11(self):
        prover = Prover()
        prover.add_formula('not(iff(K, S))')
        prover.add_formula('if(S, not(or(R, K)))')
        prover.add_goal('or(R, not(S))')
        self.assertFalse(prover.run_prover())

    def test_problem_12(self):
        prover = Prover()
        prover.add_formula('if(E, and(F, G))')
        prover.add_formula('if(F, if(G, H))')
        prover.add_goal('if(E, H)')
        self.assertTrue(prover.run_prover())

    def test_problem_13(self):
        prover = Prover()
        prover.add_formula('if(A, or(N, Q))')
        prover.add_formula('not(or(N, not(A)))')
        prover.add_goal('if(A, Q)')
        self.assertTrue(prover.run_prover())

    def test_problem_14(self):
        prover = Prover()
        prover.add_formula('if(G, H)')
        prover.add_formula('iff(R, G)')
        prover.add_formula('or(not(H), G)')
        prover.add_goal('iff(R, H)')
        self.assertTrue(prover.run_prover())

    def test_problem_15(self):
        prover = Prover()
        prover.add_formula('if(L, M)')
        prover.add_formula('if(M, N)')
        prover.add_formula('if(N, L)')
        prover.add_goal('or(L, N)')
        self.assertFalse(prover.run_prover())

    def test_problem_16(self):
        prover = Prover()
        prover.add_formula('if(S, T)')
        prover.add_formula('if(S, not(T))')
        prover.add_formula('if(not(T), S)')
        prover.add_goal('or(S, not(T))')
        self.assertFalse(prover.run_prover())

    def test_problem_17(self):
        prover = Prover()
        prover.add_formula('if(W, X)')
        prover.add_formula('if(X, W)')
        prover.add_formula('if(X, Y)')
        prover.add_formula('if(Y, X)')
        prover.add_goal('iff(W, Y)')
        self.assertTrue(prover.run_prover())

    def test_problem_18(self):
        prover = Prover()
        prover.add_formula('iff(K, or(L, M))')
        prover.add_formula('if(L, M)')
        prover.add_formula('if(M, K)')
        prover.add_formula('or(K, L)')
        prover.add_goal('if(K, L)')
        self.assertFalse(prover.run_prover())

    def test_problem_19(self):
        prover = Prover()
        prover.add_formula('if(A, B)')
        prover.add_formula('if(and(A, B), C)')
        prover.add_formula('if(A, if(C, D))')
        prover.add_goal('if(A, D)')
        self.assertTrue(prover.run_prover())

    def test_problem_20(self):
        prover = Prover()
        prover.add_formula('or(not(A), R)')
        prover.add_formula('not(and(N, not(C)))')
        prover.add_formula('if(R, C)')
        prover.add_formula('if(C, not(N))')
        prover.add_goal('or(A, C)')
        self.assertFalse(prover.run_prover())


if __name__ == '__main__':
    unittest.main()
