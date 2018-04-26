import unittest
from forseti.prover import Prover


class TestPropLogicArgumentsI(unittest.TestCase):
    def test_problem_01(self):
        prover = Prover()
        prover.add_formula('if(A, and(B, C))')
        prover.add_formula('iff(C, B)')
        prover.add_formula('not(C)')
        prover.add_goal('not(A)')
        self.assertTrue(prover.run_prover())

    def test_problem_02(self):
        prover = Prover()
        prover.add_formula('if(K, H)')
        prover.add_formula('if(H, L)')
        prover.add_formula('if(L, M)')
        prover.add_goal('if(K, M)')
        self.assertTrue(prover.run_prover())

    def test_problem_03(self):
        prover = Prover()
        prover.add_formula('not(iff(A, B))')
        prover.add_formula('not(A)')
        prover.add_formula('not(B)')
        prover.add_goal('and(C, not(C))')
        self.assertTrue(prover.run_prover())

    def test_problem_04(self):
        prover = Prover()
        prover.add_formula('and(A, or(B, C))')
        prover.add_formula('if(or(not(C), H), if(H, not(H)))')
        prover.add_goal('and(A, B)')
        self.assertFalse(prover.run_prover())

    def test_problem_05(self):
        prover = Prover()
        prover.add_formula('if(R, Q)')
        prover.add_formula('not(and(T, not(S)))')
        prover.add_formula('or(not(Q), not(S))')
        prover.add_goal('or(not(R), not(T))')
        self.assertTrue(prover.run_prover())

    def test_problem_06(self):
        prover = Prover()
        prover.add_formula('and(A, if(B, C))')
        prover.add_goal('or(and(A, B), and(A, C))')
        self.assertFalse(prover.run_prover())

    def test_problem_07(self):
        prover = Prover()
        prover.add_formula('if(and(or(C, D), H), A)')
        prover.add_formula('D')
        prover.add_goal('if(H, A)')
        self.assertTrue(prover.run_prover())

    def test_problem_08(self):
        prover = Prover()
        prover.add_formula('if(or(J, M), not(and(J, M)))')
        prover.add_formula('iff(M, if(M, J))')
        prover.add_goal('if(M, J)')
        self.assertTrue(prover.run_prover())

    def test_problem_09(self):
        prover = Prover()
        prover.add_formula('not(iff(A, B))')
        prover.add_goal('iff(not(A), not(B))')
        self.assertFalse(prover.run_prover())

    def test_problem_10(self):
        prover = Prover()
        prover.add_goal('iff(if(not(P), P), P)')
        self.assertTrue(prover.run_prover())

    def test_problem_11(self):
        prover = Prover()
        prover.add_formula('if(M, if(K, B))')
        prover.add_formula('if(not(K), not(M))')
        prover.add_formula('and(L, M)')
        prover.add_goal('B')
        self.assertTrue(prover.run_prover())

    def test_problem_12(self):
        prover = Prover()
        prover.add_formula('if(or(not(J), K), and(L, M))')
        prover.add_formula('not(or(not(J), K))')
        prover.add_goal('not(and(L, M))')
        self.assertFalse(prover.run_prover())

    def test_problem_13(self):
        prover = Prover()
        prover.add_formula('not(and(not(A), not(B)))')
        prover.add_goal('and(A, B)')
        self.assertFalse(prover.run_prover())

    def test_problem_14(self):
        prover = Prover()
        prover.add_formula('or(iff(M, K), not(and(K, D)))')
        prover.add_formula('if(not(M), not(K))')
        prover.add_formula('if(not(D), not(and(K, D)))')
        prover.add_goal('M')
        self.assertFalse(prover.run_prover())

    def test_problem_15(self):
        prover = Prover()
        prover.add_formula('and(B, or(H, Z))')
        prover.add_formula('not(if(Z, K))')
        prover.add_formula('if(iff(B, Z), not(Z))')
        prover.add_formula('not(K)')
        prover.add_goal('and(M, N)')
        self.assertTrue(prover.run_prover())

    def test_problem_16(self):
        prover = Prover()
        prover.add_formula('and(iff(D, not(G)), G)')
        prover.add_formula('if(or(G, and(if(A, D), A)), not(D))')
        prover.add_goal('if(G, not(D))')
        self.assertTrue(prover.run_prover())

    def test_problem_17(self):
        prover = Prover()
        prover.add_formula('if(J, if(T, J))')
        prover.add_formula('if(T, if(J, T))')
        prover.add_goal('and(not(J), not(T))')
        self.assertFalse(prover.run_prover())

    def test_problem_18(self):
        prover = Prover()
        prover.add_formula('and(A, if(B, C))')
        prover.add_goal('or(and(A, C), and(A, not(B)))')
        self.assertTrue(prover.run_prover())

    def test_problem_19(self):
        prover = Prover()
        prover.add_formula('or(A, not(and(B, C)))')
        prover.add_formula('not(B)')
        prover.add_formula('not(or(A, C))')
        prover.add_goal('A')
        self.assertFalse(prover.run_prover())

    def test_problem_20(self):
        prover = Prover()
        prover.add_formula('or(iff(G, H), iff(not(G), H))')
        prover.add_goal('or(iff(not(G), not(H)), not(iff(G, H)))')
        self.assertTrue(prover.run_prover())


if __name__ == '__main__':
    unittest.main()
