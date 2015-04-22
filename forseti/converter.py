"""
Converter functions for Forseti statements (to CNF)
"""

from forseti.formula import LogicalOperator, Symbol, Not, And, Or, If, Iff


def convert_to_cnf(statement):
    """
    Convert a given statement to Conjective Normal Form (CNF)

    :param statement:
    :return: a CNF statement
    """
    if isinstance(statement, Symbol):
        return statement
    elif not isinstance(statement, LogicalOperator):
        raise TypeError(str(statement) + " is not a Symbol or LogicalOperator "
                                         "Object. Use forseti.parser first")

    statement = _convert_equiv(statement)
    statement = _convert_implies(statement)
    statement = _distribute_not(statement)

    while not _is_cnf(statement):
        statement = _distribute_or(statement)

    return statement


def _convert_equiv(statement):
    """

    :param statement:
    :return:
    """
    if isinstance(statement, Symbol):
        return statement

    args = statement.args
    for i in range(len(args)):
        args[i] = _convert_equiv(args[i])

    if isinstance(statement, Iff):
        statement = And(If(args[0], args[1]), If(args[1], args[0]))

    return statement


def _convert_implies(statement):
    """

    :param statement:
    :return:
    """
    if isinstance(statement, Symbol):
        return statement

    args = statement.args
    for i in range(len(args)):
        args[i] = _convert_implies(args[i])

    if isinstance(statement, If):
        statement = Or(Not(args[0]), args[1])

    return statement


def _distribute_not(statement):
    """

    :param statement:
    :return:
    """
    if isinstance(statement, Symbol):
        return statement

    args = statement.args
    if isinstance(statement, Not):
        if isinstance(args[0], And) or isinstance(args[0], Or):
            new_type = Or
            if isinstance(args[0], Or):
                new_type = And
            args[0] = new_type(Not(args[0].args[0]), Not(args[0].args[1]))
            statement = _distribute_not(args[0])
        elif isinstance(args[0], Not):
            statement = args[0].args[0]
            statement = _distribute_not(statement)
    else:
        for i in range(len(args)):
            args[i] = _distribute_not(args[i])
    return statement


def _distribute_or(statement):
    """

    :param statement:
    :return:
    """
    if isinstance(statement, Symbol):
        return statement

    args = statement.args
    if isinstance(statement, Or):
        for i in range(len(args)):
            if isinstance(args[i], And):
                j = (i + 1) % 2
                statement = And(Or(args[i].args[0], args[j]),
                                Or(args[i].args[1], args[j]))
                break

    args = statement.args
    for i in range(len(args)):
        args[i] = _distribute_or(args[i])

    return statement


def _is_cnf(statement, has_or=False):
    """

    :param statement:
    :param has_or:
    :return:
    """
    if isinstance(statement, Symbol):
        return True
    elif isinstance(statement, If) or isinstance(statement, Iff):
        return False
    elif isinstance(statement, Or):
        has_or = True
    elif isinstance(statement, And) and has_or is True:
        return False

    args = statement.args
    for i in range(len(args)):
        if _is_cnf(args[i], has_or) is False:
            return False

    return True
