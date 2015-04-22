"""
Parser for converting plain-text to Forseti formula
"""

from forseti.formula import Symbol, Not, And, Or, If, Iff, LogicalOperator


def parse(statement):
    """
    Parse a plain-text string into Forseti formula

    TODO: raise exception on invalid formulas

    :param statement:
    :return: Predicate
    """
    if isinstance(statement, LogicalOperator) or isinstance(statement, Symbol):
        return statement
    elif statement is None or not isinstance(statement, str):
        raise TypeError("Statement cannot be " + str(type(statement)))

    original = statement
    statement = statement.replace(" ", "")

    if statement.count("(") > statement.count(")"):
        raise SyntaxError("Invalid formula (check parentheses): " + original)

    if len(statement) == 0 or statement == "()":
        raise SyntaxError("Invalid formula: " + original)

    while statement[0] == "(" and statement[-1] == ")":
        statement = statement[1:-1]

    parse_type = _get_type(statement)
    parsed_statement = _parse_statement(statement, parse_type)
    if parsed_statement is None:
        raise SyntaxError("Invalid formula: " + original)
    else:
        return parsed_statement


def _parse_statement(statement, parse_type):
    """
    Break the string into arguments to pass into the given statement

    :param statement:
    :param statement:
    :return:
    """
    if parse_type == Symbol:
        symbol_string = ""
        for char in statement:
            if not char.isalnum():
                return None
            symbol_string += char
        return Symbol(symbol_string)
    else:
        statement = statement[len(parse_type.name):]
        if len(statement) > 2 and statement[0] == "(" and statement[-1] == ")":
            statement = statement[1:-1]
            arg_list = []
            status = _get_arg_list(arg_list, statement)
            if status is False or len(arg_list) != parse_type.arity:
                return None
            return parse_type(*arg_list)
        else:
            return None


def _get_arg_list(arg_list, string):
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
            arg_list.append(parse(arg))
            arg = ""
        else:
            arg += char
        i += 1
    arg_list.append(parse(arg))
    return True


def _get_type(statement):
    """
    Get the formula type for parsing

    :param statement:
    :return:
    """
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
    else:
        parse_type = Symbol
    return parse_type

