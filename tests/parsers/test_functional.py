# pylint: disable=missing-docstring

import unittest
from forseti import parser
from forseti.formula import Symbol, Not, And, Or, If, Iff, Universal, \
    Predicate, Skolem, Herbrand


class FunctionalTester(unittest.TestCase):
    def test_parse_symbol(self):
        statement = parser.parse("a")
        self.assertEqual(statement, Symbol("a"))


    def test_parse_not(self):
        statement = parser.parse("not(a)")
        self.assertEqual(statement, Not(Symbol("a")))


    def test_parse_and(self):
        statement = parser.parse("and(a, b)")
        self.assertEqual(statement, And(Symbol("a"), Symbol("b")))


    def test_parse_or(self):
        statement = parser.parse("or(a, b)")
        self.assertEqual(statement, Or(Symbol("a"), Symbol("b")))


    def test_parse_if(self):
        statement = parser.parse("if(a, b)")
        self.assertEqual(statement, If(Symbol("a"), Symbol("b")))


    def test_parse_iff(self):
        statement = parser.parse("iff(a, b)")
        self.assertEqual(statement, Iff(Symbol("a"), Symbol("b")))


    def test_parse_iff_2(self):
        statement = parser.parse("iff(not(A), not(B))")
        self.assertEqual(statement, Iff(Not(Symbol("A")), Not(Symbol("B"))))


    def test_extra_paranthesis(self):
        statement = parser.parse("and((a),((b)))")
        self.assertEqual(And(Symbol("a"), Symbol("b")), statement)

    def test_parse_fol_1(self):
        Predicate.reset()
        Herbrand.reset()
        Skolem.reset()
        statement = parser.parse("forall(x,if(A(x),and(B(x),C(x))))")
        expected = Universal(Symbol("x"), If(Predicate("A", [Symbol("x")]),
                                             And(Predicate("B", [Symbol("x")]),
                                                 Predicate("C", [Symbol("x")]))))

        self.assertEqual(expected, statement)

    def test_empty_parse(self):
        with self.assertRaises(SyntaxError):
            parser.parse("")

    def test_bad_symbol(self):
        with self.assertRaises(SyntaxError):
            parser.parse("&a")

    def test_bad_paranthesis(self):
        with self.assertRaises(SyntaxError):
            parser.parse("and((a)),b)")

    def test_bad_paranthesis_left(self):
        with self.assertRaises(SyntaxError):
            parser.parse("and(a,b")

    def test_wrong_number_arguments(self):
        with self.assertRaises(SyntaxError):
            parser.parse("and(a)")

    def test_invalid_formula(self):
        with self.assertRaises(SyntaxError):
            parser.parse("not(a),")

    def test_extra_comma(self):
        with self.assertRaises(SyntaxError):
            parser.parse("and(a!,b)")


if __name__ == "__main__":
    unittest.main()
