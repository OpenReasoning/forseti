# pylint: disable=missing-docstring

import unittest
from forseti.formula import Symbol, Not, And, Or, Iff
from forseti import converter, parser


class TestConverter(unittest.TestCase):
    def test_cnf_converter_symbol(self):
        statement = Symbol("a")
        statement = converter.convert_formula(statement)
        expected = Symbol("a")
        self.assertEqual(expected, statement)

    def test_cnf_converter_equiv(self):
        statement = Iff(Symbol("a"), Symbol("b"))
        statement = converter.convert_formula(statement)
        expected = And(Or(Not(Symbol("a")), Symbol("b")),
                       Or(Not(Symbol("b")), Symbol("a")))
        self.assertEqual(expected, statement)

    def test_cnf_not_distribution(self):
        statement = Not(And(Symbol("a"), Symbol("b")))
        statement = converter.convert_formula(statement)
        expected = Or(Not(Symbol("a")), Not(Symbol("b")))
        self.assertEqual(expected, statement)

    def test_cnf_not_distribution_2(self):
        statement = Not(Or(And(Symbol("a"), Not(Symbol("b"))), Not(Symbol("c"))))
        statement = converter.convert_formula(statement)
        expected = And(Or(Not(Symbol("a")), Symbol("b")), Symbol("c"))
        self.assertEqual(expected, statement)

    def test_cnf_or_distribution(self):
        statement = Or(And(Symbol("a"), Symbol("b")), Symbol("c"))
        statement = converter.convert_formula(statement)
        expected = And(Or(Symbol("a"), Symbol("c")), Or(Symbol("b"), Symbol("c")))
        self.assertEqual(expected, statement)

    def test_cnf_negation(self):
        statement = Not(Not(And(Symbol("a"), Symbol("b"))))
        statement = converter.convert_formula(statement)
        expected = And(Symbol("a"), Symbol("b"))
        self.assertEqual(expected, statement)

    def test_convert_to_cnf(self):
        statement = Not(Iff(Symbol("a"), Symbol("c")))
        statement = converter.convert_formula(statement)
        a_symbol = Symbol("a")
        c_symbol = Symbol("c")
        expected = And(And(Or(c_symbol, a_symbol), Or(Not(a_symbol), a_symbol)),
                       And(Or(c_symbol, Not(c_symbol)), Or(Not(a_symbol),
                                                           Not(c_symbol))))
        self.assertEqual(expected, statement)

    def test_convert_to_cnf_2(self):
        statement = parser.parse("forall(x,if(A(x),and(B(x),C(x))))")
        statement = converter.convert_formula(statement)
        expected = "((B(Herbrand1) | ~A(Herbrand1)) & (C(Herbrand1) | ~A(Herbrand1)))"
        self.assertEqual(expected, str(statement))

    def test_cnf_error_on_string(self):
        with self.assertRaises(TypeError):
            converter.convert_formula("invalid")


if __name__ == "__main__":
    unittest.main()
