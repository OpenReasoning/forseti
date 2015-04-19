"""
Util functions utilized by Forseti library (or for testing it)
"""

from __future__ import print_function
from forseti.formula import Not, LogicalOperator, Symbol
import sys


def print_cnf_list(formulas, depth=0, end="\n", out=sys.stdout):
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
        output += ", "
    output = output[:-2] + "]"
    if depth > 0:
        return output
    else:
        out.write(output+end)


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


def is_tautology(cnf):
    """
    Checks if a given CNF is a tautology
    :return boolean: True if it is a tautology, false otherwise
    """
    if not isinstance(cnf, list) or len(cnf) <= 1:
        return False
    i = 0
    while i < len(cnf):
        if negate_formula(cnf[i]) in cnf:
            return True
        i += 1
    return False
