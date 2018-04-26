"""
Tests to ensure that LogicalOperator representation works as expected
"""
# pylint: disable=missing-docstring,expression-not-assigned

import unittest
from forseti.formula import Formula, Symbol, LogicalOperator, Not, And, Or, If, Iff


class TestFormula(unittest.TestCase):
    def test_formula_str(self):
        with self.assertRaises(NotImplementedError):
            str(Formula())

    def test_formula_repr(self):
        with self.assertRaises(NotImplementedError):
            repr(Formula())

    def test_formula_eq(self):
        with self.assertRaises(NotImplementedError):
            # noinspection PyStatementEffect
            Formula() == Formula()

    def test_formula_ne(self):
        with self.assertRaises(NotImplementedError):
            # noinspection PyStatementEffect
            Formula() != Formula()

    def test_formula_lt(self):
        with self.assertRaises(NotImplementedError):
            # noinspection PyStatementEffect
            Formula() < Formula()

    def test_formula_le(self):
        with self.assertRaises(NotImplementedError):
            # noinspection PyStatementEffect
            Formula <= Formula()

    def test_formula_gt(self):
        with self.assertRaises(NotImplementedError):
            # noinspection PyStatementEffect
            Formula() > Formula()

    def test_formula_ge(self):
        with self.assertRaises(NotImplementedError):
            # noinspection PyStatementEffect
            Formula >= Formula()

    def test_abstract_str(self):
        with self.assertRaises(NotImplementedError):
            statement = LogicalOperator()
            str(statement)

    def test_abstract_repr(self):
        with self.assertRaises(NotImplementedError):
            statement = LogicalOperator()
            repr(statement)

    def test_invalid_statement(self):
        with self.assertRaises(TypeError):
            LogicalOperator("a")

    def test_symbol(self):
        statement = Symbol('a')
        self.assertEqual(statement.arity, 0)
        self.assertEqual(repr(statement), "a")
        self.assertEqual(str(statement), "a")

    def test_not(self):
        statement_a = Symbol('a')
        statement_not = Not(statement_a)
        self.assertEqual(statement_not.arity, 1)
        self.assertEqual(repr(statement_not), "not(a)")
        self.assertEqual(str(statement_not), "~a")

    def test_and(self):
        statement_a = Symbol('a')
        statement_b = Symbol('b')
        statement_and = And(statement_a, statement_b)
        self.assertEqual(statement_and.arity, 2)
        self.assertEqual(repr(statement_and), "and(a, b)")
        self.assertEqual(str(statement_and), "(a & b)")

    def test_or(self):
        statement_a = Symbol('a')
        statement_b = Symbol('b')
        statement_or = Or(statement_a, statement_b)
        self.assertEqual(statement_or.arity, 2)
        self.assertEqual(repr(statement_or), "or(a, b)")
        self.assertEqual(str(statement_or), "(a | b)")

    def test_if(self):
        statement_a = Symbol('a')
        statement_b = Symbol('b')
        statement_if = If(statement_a, statement_b)
        self.assertEqual(statement_if.arity, 2)
        self.assertEqual(repr(statement_if), "if(a, b)")
        self.assertEqual(str(statement_if), "(a -> b)")

    def test_iff(self):
        statement_a = Symbol('a')
        statement_b = Symbol('b')
        statement_iff = Iff(statement_a, statement_b)
        self.assertEqual(statement_iff.arity, 2)
        self.assertEqual(repr(statement_iff), "iff(a, b)")
        self.assertEqual(str(statement_iff), "(a <-> b)")

    def test_complex(self):
        statement_a = Symbol('a')
        statement_b = Symbol('b')
        statement_and = And(statement_a, statement_b)
        statement_or = Or(statement_and, statement_a)
        statement_implies = If(statement_or, statement_and)
        statement_equiv = Iff(statement_implies, statement_a)
        self.assertEqual(repr(statement_equiv), "iff(if(or(and(a, b), a), "
                                                "and(a, b)), a)")
        self.assertEqual(str(statement_equiv), "((((a & b) | a) -> (a & b)) <-> a)")

    def test_equality(self):
        statement_a = Symbol('a')
        statement_b = Symbol('b')
        statement_and = And(statement_a, statement_b)
        statement_or = Or(statement_and, statement_a)
        statement_if = If(statement_or, statement_and)
        statement_iff = Iff(statement_if, statement_a)
        expected = Iff(If(Or(And(Symbol("a"), Symbol("b")), Symbol("a")),
                          And(Symbol("a"), Symbol("b"))), Symbol("a"))
        self.assertTrue(expected == statement_iff)
        self.assertEqual(repr(expected), repr(statement_iff))
        self.assertEqual(str(expected), str(statement_iff))

    def test_non_equality(self):
        statement_a = Symbol('a')
        statement_b = Symbol('b')
        statement_and = And(statement_a, statement_b)
        statement_or = Or(statement_and, statement_b)
        self.assertNotEqual(statement_or, Or(And(Symbol('a'), Symbol('b')), Symbol('a')))

    def test_non_equality_2(self):
        statement_1 = Not(Symbol("b"))
        statement_2 = Symbol("a")
        self.assertNotEqual(statement_1, statement_2)

    def test_non_equality_symbol(self):
        self.assertNotEqual(Symbol("a"), Symbol("b"))

    def test_non_equality_symbol_string(self):
        self.assertNotEqual(Symbol("a"), "a")

    def test_equality_false_symbol_type(self):
        self.assertFalse(Symbol("a") == "a")

    def test_bad_symbol(self):
        with self.assertRaises(TypeError):
            Symbol(Symbol('a'))

    def test_symbol_lt_symbol_1(self):
        self.assertLess(Symbol('a'), Symbol('b'))

    def test_symbol_lt_operator_1(self):
        self.assertLess(Symbol('a'), Not(Symbol('a')))

    def test_symbol_le_symbol(self):
        self.assertLessEqual(Symbol('a'), Symbol('b'))

    def test_symbol_gt_symbol(self):
        self.assertGreater(Symbol('b'), Symbol('a'))

    def test_symbol_ge_operator_1(self):
        self.assertGreaterEqual(Symbol('b'), Symbol('a'))

    def test_operator_not_lt_symbol(self):
        self.assertFalse(Not(Symbol("a")) < Symbol("b"))

    def test_operator_le_symbol(self):
        self.assertLessEqual(Not(Symbol('a')), Not(Symbol('b')))

    def test_operator_gt_symbol(self):
        self.assertGreater(Not(Symbol("a")), Symbol("b"))

    def test_operator_ge_symbol(self):
        self.assertGreaterEqual(Not(Symbol("a")), Not(Symbol("a")))


if __name__ == "__main__":
    unittest.main()
