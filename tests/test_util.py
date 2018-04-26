# pylint: disable=missing-docstring

from io import StringIO
import unittest
from forseti.formula import Symbol, Not, Or
import forseti.util as util


class TestUtil(unittest.TestCase):
    def test_print_cnf_list(self):
        cnf = list()
        a_symbol = Symbol("a")
        b_symbol = Symbol("b")
        not_a = Not(a_symbol)
        not_b = Not(b_symbol)
        cnf.append([a_symbol, b_symbol])
        cnf.append([not_b, a_symbol])
        cnf.append([not_a, not_b])
        writer = StringIO()
        util.print_cnf_list(cnf, out=writer)
        cnf_list = "[[a, b], [~b, a], [~a, ~b]]\n"
        self.assertEqual(cnf_list, writer.getvalue())

    def test_cnf_list_as_disjunction(self):
        cnf = [Symbol("a"), Symbol("b")]
        expected = util.cnf_list_as_disjunction(cnf)
        self.assertEqual(expected, Or(Symbol("a"), Symbol("b")))

    def test_cnf_list_empty(self):
        self.assertEqual(util.cnf_list_as_disjunction([]), "$$FALSE")

    def test_negate_symbol(self):
        negate = util.negate_formula(Symbol("a"))
        self.assertEqual(Not(Symbol("a")), negate)

    def test_negate_not(self):
        negate = util.negate_formula(Not(Symbol("a")))
        self.assertEqual(Symbol("a"), negate)

    def test_negate_error(self):
        with self.assertRaises(TypeError):
            util.negate_formula("a")

    def test_is_tautology(self):
        cnf = list()
        cnf.append(Symbol("a"))
        cnf.append(Not(Symbol("a")))
        is_taut = util.is_tautology(cnf)
        self.assertTrue(is_taut)

    def test_is_tautology_negative(self):
        cnf = list()
        cnf.append(Symbol("a"))
        cnf.append(Symbol("b"))
        is_taut = util.is_tautology(cnf)
        self.assertFalse(is_taut)

    def test_is_tautology_bad_input(self):
        self.assertFalse(util.is_tautology("a"))
        self.assertFalse(util.is_tautology([Symbol("a")]))


if __name__ == "__main__":
    unittest.main()
