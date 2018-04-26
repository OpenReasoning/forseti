"""
Class of propositional logic problems that are defined within handouts/PropLogicProofs.pdf
"""
import unittest

from forseti.prover import Prover


class TestPropLogicProofsI(unittest.TestCase):
    def test_problem_01(self):
        prover = Prover()
        prover.add_formula("and(R, and(C, not(F)))")
        prover.add_formula("if(or(R, S), not(W))")
        prover.add_goal("not(W)")
        self.assertTrue(prover.run_prover())

    def test_problem_02(self):
        prover = Prover()
        prover.add_formula("if(A, and(B, C))")
        prover.add_formula("not(C)")
        prover.add_goal("not(and(A, D))")
        self.assertTrue(prover.run_prover())

    def test_problem_03(self):
        prover = Prover()
        prover.add_formula("not(iff(A, B))")
        prover.add_formula("not(A)")
        prover.add_formula("not(B)")
        prover.add_goal("and(C, not(C))")
        self.assertTrue(prover.run_prover())

    def test_problem_04(self):
        prover = Prover()
        prover.add_formula("iff(F, G)")
        prover.add_formula("or(F, G)")
        prover.add_goal("and(F, G)")
        self.assertTrue(prover.run_prover())

    def test_problem_05(self):
        prover = Prover()
        prover.add_formula("iff(not(B), Z)")
        prover.add_formula("if(N, B)")
        prover.add_formula("and(Z, N)")
        prover.add_goal("not(H)")
        self.assertTrue(prover.run_prover())

    def test_problem_06(self):
        prover = Prover()
        prover.add_formula("iff(A, B)")
        prover.add_formula("iff(B, not(C))")
        prover.add_goal("not(iff(A, C))")
        self.assertTrue(prover.run_prover())

    def test_problem_07(self):
        prover = Prover()
        prover.add_formula("if(M, I)")
        prover.add_formula("and(not(I), L)")
        prover.add_formula("or(M, B)")
        prover.add_goal("B")
        self.assertTrue(prover.run_prover())

    def test_problem_08(self):
        prover = Prover()
        prover.add_formula("or(Q, iff(J, D))")
        prover.add_formula("not(D)")
        prover.add_formula("J")
        prover.add_goal("Q")
        self.assertTrue(prover.run_prover())

    def test_problem_09(self):
        prover = Prover()
        prover.add_formula("or(A, B)")
        prover.add_formula("or(not(B), C)")
        prover.add_formula("not(C)")
        prover.add_goal("A")
        self.assertTrue(prover.run_prover())

    def test_problem_10(self):
        prover = Prover()
        prover.add_formula("or(or(not(H), J), K)")
        prover.add_formula("if(K, not(I))")
        prover.add_goal("if(and(H, I), J)")
        self.assertTrue(prover.run_prover())

    def test_problem_11(self):
        prover = Prover()
        prover.add_formula("and(or(A, B), not(C))")
        prover.add_formula("if(not(C), and(D, not(A)))")
        prover.add_formula("if(B, or(A, E))")
        prover.add_goal("or(E, F)")
        self.assertTrue(prover.run_prover())

    def test_problem_12(self):
        prover = Prover()
        prover.add_formula("if(G, and(H, not(K)))")
        prover.add_formula("iff(H, and(L, I))")
        prover.add_formula("or(not(I), K)")
        prover.add_goal("not(G)")
        self.assertTrue(prover.run_prover())

    def test_problem_13(self):
        prover = Prover()
        prover.add_formula("if(R, and(not(A), T))")
        prover.add_formula("or(B, not(S))")
        prover.add_formula("or(B, S)")
        prover.add_goal("if(A, B)")
        self.assertTrue(prover.run_prover())

    def test_problem_14(self):
        prover = Prover()
        prover.add_formula("or(S, and(not(R), T))")
        prover.add_formula("if(R, not(S))")
        prover.add_goal("not(R)")
        self.assertTrue(prover.run_prover())

    def test_problem_15(self):
        prover = Prover()
        prover.add_formula("if(K, if(or(L, M), R))")
        prover.add_formula("if(or(R, S), T)")
        prover.add_goal("if(K, if(M, T))")
        self.assertTrue(prover.run_prover())

    def test_problem_16(self):
        prover = Prover()
        prover.add_formula("and(or(P, R), or(P, Q))")
        prover.add_formula("if(and(Q, R), if(V, W))")
        prover.add_formula("not(if(if(P, S), not(if(S, W))))")
        prover.add_formula("not(W)")
        prover.add_goal("if(V, S)")
        self.assertTrue(prover.run_prover())

    def test_problem_17(self):
        prover = Prover()
        prover.add_formula("if(and(A, B), C)")
        prover.add_formula("if(not(A), C)")
        prover.add_formula("B")
        prover.add_goal("C")
        self.assertTrue(prover.run_prover())

    def test_problem_18(self):
        prover = Prover()
        prover.add_formula("or(F, G)")
        prover.add_formula("and(H, if(I, F))")
        prover.add_formula("if(H, not(F))")
        prover.add_goal("and(G, not(I))")
        self.assertTrue(prover.run_prover())

    def test_problem_19(self):
        prover = Prover()
        prover.add_formula("if(if(R, M), L)")
        prover.add_formula("if(or(N, S), and(M, T))")
        prover.add_formula("if(if(P, R), L)")
        prover.add_formula("if(or(T, K), not(N))")
        prover.add_goal("L")
        self.assertTrue(prover.run_prover())

    def test_problem_20(self):
        prover = Prover()
        prover.add_formula("iff(N, P)")
        prover.add_goal("iff(if(N, R), if(P, R))")
        self.assertTrue(prover.run_prover())

if __name__ == "__main__":
    unittest.main()
