"""
Class of propositional logic problems that are defined within handouts/PropLogicProofsII.pdf
"""
import unittest
from forseti.prover import Prover


class TestPropLogicProofsII(unittest.TestCase):
    def test_problem_01(self):
        prover = Prover()
        prover.add_formula("not(A)")
        prover.add_goal("if(A, B)")
        self.assertTrue(prover.run_prover())

    def test_problem_02(self):
        prover = Prover()
        prover.add_formula("A")
        prover.add_goal("if(B, A)")
        self.assertTrue(prover.run_prover())

    def test_problem_03(self):
        prover = Prover()
        prover.add_formula("if(A, if(B, C))")
        prover.add_goal("if(B, if(A, C))")
        self.assertTrue(prover.run_prover())

    def test_problem_04(self):
        prover = Prover()
        prover.add_formula("if(A, B)")
        prover.add_formula("if(A, C)")
        prover.add_goal("if(A, and(B, C))")
        self.assertTrue(prover.run_prover())

    def test_problem_05(self):
        prover = Prover()
        prover.add_formula("if(A, C)")
        prover.add_formula("if(B, C)")
        prover.add_goal("if(or(A, B), C)")
        self.assertTrue(prover.run_prover())

    def test_problem_06(self):
        prover = Prover()
        prover.add_formula("or(A, and(B, C))")
        prover.add_formula("if(A, D)")
        prover.add_formula("if(D, C)")
        prover.add_goal("C")
        self.assertTrue(prover.run_prover())

    def test_problem_07(self):
        prover = Prover()
        prover.add_formula("A")
        prover.add_formula("iff(A, B)")
        prover.add_formula("if(C, not(B))")
        prover.add_goal("not(C)")
        self.assertTrue(prover.run_prover())

    def test_problem_08(self):
        prover = Prover()
        prover.add_formula("if(or(A, B), if(C, D))")
        prover.add_formula("if(or(not(D), E), and(A, C))")
        prover.add_goal("D")
        self.assertTrue(prover.run_prover())

    def test_problem_09(self):
        prover = Prover()
        prover.add_formula("if(A, B)")
        prover.add_formula("if(A, not(B))")
        prover.add_goal("not(A)")
        self.assertTrue(prover.run_prover())

    def test_problem_10(self):
        prover = Prover()
        prover.add_formula("or(not(A), B)")
        prover.add_formula("or(A, C)")
        prover.add_formula("if(not(D), not(C))")
        prover.add_goal("or(B, D)")
        self.assertTrue(prover.run_prover())

    def test_problem_11(self):
        prover = Prover()
        prover.add_formula("if(A, not(if(B, C)))")
        prover.add_formula("if(and(D, B), C)")
        prover.add_formula("D")
        prover.add_goal("not(A)")
        self.assertTrue(prover.run_prover())

    def test_problem_12(self):
        prover = Prover()
        prover.add_formula("if(A, B)")
        prover.add_formula("if(not(B), not(C))")
        prover.add_formula("not(and(not(C), not(A)))")
        prover.add_goal("B")
        self.assertTrue(prover.run_prover())

    def test_problem_13(self):
        prover = Prover()
        prover.add_formula("if(A, B)")
        prover.add_formula("if(not(C), not(B))")
        prover.add_formula("iff(C, D)")
        prover.add_goal("if(A, D)")
        self.assertTrue(prover.run_prover())

    def test_problem_14(self):
        prover = Prover()
        prover.add_formula("if(or(A, not(A)), not(B))")
        prover.add_formula("if(and(C, D), B)")
        prover.add_goal("or(not(D), not(C))")
        self.assertTrue(prover.run_prover())

    def test_problem_15(self):
        prover = Prover()
        prover.add_formula("if(or(not(A), B), and(C, D))")
        prover.add_formula("not(or(A, E))")
        prover.add_formula("if(F, not(D))")
        prover.add_goal("not(F)")
        self.assertTrue(prover.run_prover())

    def test_problem_16(self):
        prover = Prover()
        prover.add_formula("iff(not(or(A, not(B))), not(C))")
        prover.add_formula("C")
        prover.add_goal("if(B, or(A, D))")
        self.assertTrue(prover.run_prover())

    def test_problem_17(self):
        prover = Prover()
        prover.add_formula("and(A, and(B, C))")
        prover.add_formula("if(A, or(D, E))")
        prover.add_formula("if(B, or(D, F))")
        prover.add_goal("or(D, and(E, F))")
        self.assertTrue(prover.run_prover())

    def test_problem_18(self):
        prover = Prover()
        prover.add_formula("if(and(A, B), C)")
        prover.add_formula("and(not(C), B)")
        prover.add_formula("if(or(not(A), D), E)")
        prover.add_goal("E")
        self.assertTrue(prover.run_prover())

    def test_problem_19(self):
        prover = Prover()
        prover.add_formula("if(A, and(B, C))")
        prover.add_formula("if(or(B, D), A)")
        prover.add_goal("iff(A, B)")
        self.assertTrue(prover.run_prover())

    def test_problem_20(self):
        """
        While the PDF claims all arguments are "valid", this one is not
        """
        prover = Prover()
        prover.add_formula("if(or(not(A), B), not(and(C, D)))")
        prover.add_formula("if(and(A, C), E)")
        prover.add_formula("and(A, not(E))")
        prover.add_goal("not(or(D, E))")
        self.assertFalse(prover.run_prover())


if __name__ == "__main__":
    unittest.main()
