"""
Util functions utilized by Forseti library (or for testing it)
"""

from __future__ import print_function
from forseti.formula import Not, LogicalOperator, Symbol


def print_cnf_list(formulas, depth=0, end="\n"):
    """
    prints out the CNF list

    :param formulas:
    :return:
    """
    output = "["
    for i in formulas:
        if isinstance(i, list):
            output += print_cnf_list(i, depth=depth+1)
        else:
            output += str(i)
        output += ","
    output = output[:-1] + "]"
    if depth > 0:
        return output
    else:
        print(output, end=end)


def negate_formula(formula):
    """
    Negate the formula (or removing the Not if it's the outermost Operator)

    :param formula: formula
    :return: Negated formula
    """
    if isinstance(formula, Not):
        return formula.args[0]
    elif isinstance(formula, Symbol) or isinstance(formula, LogicalOperator):
        return Not(formula)
    else:
        raise TypeError(str(formula) + " is not a valid formula "
                                       "(Symbol or Operator)")
