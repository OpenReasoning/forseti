"""
Converter functions for Forseti statements (to CNF)
"""

from .formula import Formula, Symbol, LogicalOperator, Not, And, Or, \
    If, Iff, Quantifier, Existential, Skolem, Universal, Herbrand
import forseti.parser as parser


def convert_formula(statement):
    """
    Converts a given formula into something we can use
    as CNF clauses for resolution

    :param statement:
    :return: a CNF statement
    """
    if isinstance(statement, Symbol):
        return statement
    elif not isinstance(statement, Formula):
        raise TypeError(str(statement) + " is not a Symbol or LogicalOperator "
                                         "Object. Use forseti.parser first")

    statement = _convert_iff(statement)
    while not _is_pnf(statement):
        statement = _convert_pnf(statement)
    statement = _convert_if(statement)
    statement = _distribute_not(statement)
    statement = _skolemization(statement)
    statement = _herbrandization(statement)

    while not _is_cnf(statement):
        statement = _distribute_or(statement)

    return statement


def _convert_iff(statement):
    """
    Convert biconditionals into two conditionals joined by an And

    :param statement:
    :return:
    """
    if isinstance(statement, Symbol):
        return statement

    args = statement.args
    for i in range(len(args)):
        args[i] = _convert_iff(args[i])

    if isinstance(statement, Iff):
        statement = And(If(args[0], args[1]), If(args[1], args[0]))

    return statement


def _convert_if(statement):
    """
    Convert conditional (A -> B) into (~A or B)

    :param statement:
    :return:
    """
    if isinstance(statement, Symbol):
        return statement

    args = statement.args
    for i in range(len(args)):
        args[i] = _convert_if(args[i])

    if isinstance(statement, If):
        statement = Or(Not(args[0]), args[1])

    return statement


def _distribute_not(statement):
    """
    Distribute not over and/or clauses (flipping them)

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
            statement = new_type(Not(args[0].args[0]), Not(args[0].args[1]))
            statement = _distribute_not(statement)
        elif isinstance(args[0], Not):
            statement = args[0].args[0]
            statement = _distribute_not(statement)
        elif isinstance(args[0], Quantifier):
            new_type = Existential
            if isinstance(args[0], Existential):
                new_type = Universal
            statement = new_type(args[0].symbol, Not(args[0].args[0]))
            statement.args[0] = _distribute_not(statement.args[0])
    else:
        for i in range(len(args)):
            args[i] = _distribute_not(args[i])
    return statement


def _distribute_or(statement):
    """
    Distribute or over any nested and statements (so and becomes
    outer most logical operator)

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
    Is the given formula a CNF yet?

    :param statement:
    :param has_or:
    :return:
    """
    if isinstance(statement, Symbol) or isinstance(statement, Herbrand)\
            or isinstance(statement, Skolem):
        return True
    elif isinstance(statement, Or):
        has_or = True
    elif isinstance(statement, And) and has_or is True:
        return False

    args = statement.args
    for i in range(len(args)):
        if _is_cnf(args[i], has_or) is False:
            return False

    return True


def _convert_pnf(statement):
    """
    Covert a formula into PNF form. Needs to be run after _convert_if!

    :param statement:
    :return:
    """
    if isinstance(statement, str) or isinstance(statement, Symbol) or isinstance(statement, Herbrand) or isinstance(statement, Skolem):
        return statement
    if isinstance(statement, LogicalOperator):
        if isinstance(statement, If):
            if isinstance(statement.args[0], Existential):
                statement = Universal(statement.args[0].symbol, If(statement.args[0].args[0], statement.args[1]))
            elif isinstance(statement.args[0], Universal):
                statement = Existential(statement.args[0].symbol, If(statement.args[0].args[0], statement.args[1]))
            elif isinstance(statement.args[1], Quantifier):
                q_type = type(statement.args[1])
                statement = q_type(statement.args[1].symbol, If(statement.args[0], statement.args[1].args[0]))
        elif isinstance(statement, And):
            if isinstance(statement.args[0], Quantifier):
                q_type = type(statement.args[0])
                statement = q_type(statement.args[0].symbol, And(statement.args[0].args[0], statement.args[1]))
            elif isinstance(statement.args[1], Quantifier):
                q_type = type(statement.args[1])
                statement = q_type(statement.args[1].symbol, And(statement.args[0], statement.args[1].args[0]))
        elif isinstance(statement, Or):
            if isinstance(statement.args[0], Quantifier):
                q_type = type(statement.args[0])
                statement = q_type(statement.args[0].symbol, Or(statement.args[0].args[0], statement.args[1]))
            elif isinstance(statement.args[1], Quantifier):
                q_type = type(statement.args[1])
                statement = q_type(statement.args[1].symbol, Or(statement.args[0], statement.args[1].args[0]))
        elif isinstance(statement, Not):
            if isinstance(statement.args[0], Existential):
                statement = Universal(statement.args[0].symbol, Not(statement.args[0].args[0]))
            elif isinstance(statement.args[0], Universal):
                statement = Existential(statement.args[0].symbol, Not(statement.args[0].args[0]))

    for i in range(len(statement.args)):
        statement.args[i] = _convert_pnf(statement.args[i])
    return statement


def _is_pnf(statement, has_operator=False):
    """
    Is the given statement a PNF yet?

    :param statement:
    :param has_operator:
    :return:
    """
    if isinstance(statement, Symbol) or isinstance(statement, Herbrand) \
            or isinstance(statement, Skolem):
        return True
    elif isinstance(statement, LogicalOperator):
        has_operator = True
    elif isinstance(statement, Quantifier) and has_operator:
        return False

    args = statement.args
    for i in range(len(args)):
        if _is_pnf(args[i], has_operator) is False:
            return False
    return True


def _skolemization(statement, exists=None):
    """
    Remove existential quantifiers through skolemization

    If the existential is inside

    :param statement:
    :param exists: dictionary containing what skole to replace a variable with
                    x -> Skole1
                    y -> Skole2
                    etc.
    :return:
    """
    if exists is None:
        exists = dict()
    if isinstance(statement, Existential):
        exists[statement.symbol] = Skolem()
        statement = _skolemization(statement.args[0], exists)
    elif isinstance(statement, Universal):
        statement.args[0] = _skolemization(statement.args[0], exists)
    elif isinstance(statement, Formula):
        for i in range(len(statement.args)):
            if isinstance(statement.args[i], Symbol):
                if statement.args[i].arg in exists:
                    statement.args[i] = exists[str(statement.args[i])]
            else:
                statement.args[i] = _skolemization(statement.args[i], exists)
    else:
        if statement in exists:
            statement = exists[str(statement)]
    return statement


def _herbrandization(statement, forall=None):
    """
    Remove universal quantifiers through herbrandization

    :param statement:
    :param forall:
    :return:
    """
    if forall is None:
        forall = dict()
    if isinstance(statement, Universal):
        forall[statement.symbol] = Herbrand()
        statement = _herbrandization(statement.args[0], forall)
    elif isinstance(statement, Existential):
        statement.args[0] = _herbrandization(statement.args[0], forall)
    elif isinstance(statement, Formula):
        for i in range(len(statement.args)):
            if isinstance(statement.args[i], Symbol):
                if statement.args[i].arg in forall:
                    statement.args[i] = forall[str(statement.args[i])]
            else:
                statement.args[i] = _herbrandization(statement.args[i], forall)
    else:
        if statement in forall:
            statement = forall[str(statement)]
    return statement

if __name__ == "__main__":
    print(convert_formula(parser.parse("not(forall(x,if(A(x),C(x))))")))