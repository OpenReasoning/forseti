"""
Module that contains a functional form parser

Acceptable inputs to this parser are:
A
not(A)
and(A, B)
or(A, B)
if(A, B)
iff(A, B)
"""

from ..formula import Symbol, Not, And, Or, If, Iff, Predicate, Existential, Universal
from forseti.parsers.abstract_parser import AbstractParser


class FunctionalParser(AbstractParser):
    """

    """
    @staticmethod
    def parse(statement, formula_types):
        """
        Internal parse function

        :param statement:
        :param formula_types:
        :return:
        """
        original = statement
        statement = statement.replace(" ", "")

        if statement.count("(") > statement.count(")"):
            raise SyntaxError("Invalid formula (check parentheses): " + original)

        if len(statement) == 0 or statement == "()":
            raise SyntaxError("Invalid formula: " + original)

        while statement[0] == "(" and statement[-1] == ")":
            statement = statement[1:-1]

        parse_type = FunctionalParser._get_type(statement, formula_types)
        formula_types.append(parse_type)
        parsed_statement = FunctionalParser._parse_statement(statement, parse_type, formula_types)
        if parsed_statement is None:
            raise SyntaxError("Invalid formula: " + original)
        else:
            formula_types.pop(len(formula_types)-1)
            return parsed_statement

    @staticmethod
    def _parse_statement(statement, parse_type, formula_types):
        """
        Break the string into arguments to pass into the given statement

        :param statement:
        :param statement:
        :return:
        """
        if parse_type == Symbol:
            return FunctionalParser._get_symbol(statement)
        else:
            type_name = FunctionalParser._get_type_name(statement, parse_type)

            statement = statement[len(type_name):]

            if len(statement) > 2 and statement[0] == "(" and statement[-1] == ")":
                statement = statement[1:-1]
                arg_list = []
                status = FunctionalParser._get_arg_list(arg_list, statement, formula_types)
                if parse_type != Predicate:
                    arity = parse_type.arity
                else:
                    arity = Predicate.get_arity(type_name)

                if status is False or (-1 < arity != len(arg_list)):
                    return None
                if parse_type == Predicate:
                    return parse_type(type_name, arg_list)
                else:
                    return parse_type(*arg_list)
            else:
                return None

    @staticmethod
    def _get_arg_list(arg_list, string, formula_types):
        """
        get the argument list of a 2+ argument statement

        :param arg_list:
        :param string:
        :return:
        """
        i = 0
        open_p = 0
        arg = ""
        while i < len(string):
            char = string[i]
            if char == "(":
                open_p += 1
            elif char == ")" and open_p >= 0:
                open_p -= 1

            if not char.isalnum() and ((char != "," and char != ")") and open_p == 0):
                return False

            if char == "," and open_p == 0:
                arg_list.append(FunctionalParser.parse(arg, formula_types))
                arg = ""
            else:
                arg += char
            i += 1
        arg_list.append(FunctionalParser.parse(arg, formula_types))
        return True

    @staticmethod
    def _get_type(statement, formula_types):
        """
        Get the formula type for parsing

        :param statement:
        :return:
        """
        parse_type = None
        if Predicate not in formula_types:
            if statement.lower().startswith("and"):
                parse_type = And
            elif statement.lower().startswith("or"):
                parse_type = Or
            elif statement.lower().startswith("iff"):
                parse_type = Iff
            elif statement.lower().startswith("if"):
                parse_type = If
            elif statement.lower().startswith("not"):
                parse_type = Not
            elif statement.lower().startswith("exists"):
                parse_type = Existential
            elif statement.lower().startswith("forall"):
                parse_type = Universal
        if parse_type is None:
            if "(" in statement.lower():
                parse_type = Predicate
            else:
                parse_type = Symbol

        return parse_type

    @staticmethod
    def _get_symbol(statement):
        """
        Gets the symbol for a statement

        :param statement:
        :return:
        """
        symbol_string = ""
        for char in statement:
            if not char.isalnum():
                return None
            symbol_string += char
        return Symbol(symbol_string)

    @staticmethod
    def _get_type_name(statement, parse_type):
        """
        Get the type's name

        :param statement:
        :param parse_type:
        :return:
        """
        if parse_type == Predicate:
            type_name = ""
            for char in statement:
                if char == "(":
                    break
                type_name += char
        else:
            type_name = parse_type.name
        return type_name