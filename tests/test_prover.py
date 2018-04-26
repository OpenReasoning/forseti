# pylint: disable=missing-docstring

import unittest
from forseti.prover import Prover


class TestProver(unittest.TestCase):
    def test_get_proof(self):
        prover = Prover()
        prover.add_formula("and(a,b)")
        prover.add_goal("a")
        prover.run_prover()
        proof = prover.get_proof()
        expected = ['  1)    a                                                    '
                    '                    Assumption',
                    '  3)    ~a                                                   '
                    '                    Assumption',
                    '  4)    $$FALSE                                              '
                    '                    resolve(1,3)']
        self.assertEqual(expected, proof)

    def test_prover_formula_error(self):
        prover = Prover()
        with self.assertRaises(TypeError):
            prover.add_formula(None)

    def test_prover_no_goal_error(self):
        prover = Prover()
        with self.assertRaises(Exception):
            prover.run_prover()


if __name__ == "__main__":
    unittest.main()
