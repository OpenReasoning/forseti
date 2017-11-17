# -*- coding: utf-8 -*-
"""
Util functions utilized by Forseti library (or for testing it)
"""

from forseti.formula import Formula, Symbol, Not, And, Or, If, Iff, Herbrand, Predicate, Skolem
import sys


def print_cnf_list(formulas, depth=0, end="\n", out=sys.stdout):
    """
    prints out the CNF list

    :param formulas:
    :param depth: depth we're at within the cnf list
    :param end: line ending for cnf list
    :param out: output to write to
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


def cnf_list_as_disjunction(formulas):
    """

    :param formulas:
    :return:
    """
    if len(formulas) > 0:
        output = formulas[0]
        for i in range(1, len(formulas)):
            output = Or(output, formulas[i])
        return output
    else:
        return "$$FALSE"


def negate_formula(formula):
    """
    Negate the formula (or removing the Not if it's the outermost Operator)

    :param formula: formula
    :return: Negated formula
    """
    if isinstance(formula, Not):
        return formula.args[0]
    elif isinstance(formula, Formula):
        return Not(formula)
    else:
        raise TypeError(str(formula) + " is not a valid formula")


def is_tautology(cnf):
    """
    Checks if a given CNF is a tautology
    :return boolean: True if it is a tautology, false otherwise
    """
    if not isinstance(cnf, list) or len(cnf) <= 1:
        return False
    i = 0
    while i < len(cnf):
        if _in_list(cnf, negate_formula(cnf[i])):
            return True
        i += 1
    return False


def _in_list(cnf_list, negation):
    """

    :param cnf_list:
    :param negation:
    :return:
    """
    for i in range(len(cnf_list)):
        element = cnf_list[i]
        run = _check_element(element, negation)
        if run is True:
            return True
    return False


def _check_element(element, negation):
    """

    :param element:
    :param negation:
    :return:
    """
    if isinstance(element, type(negation)) and not isinstance(element, Herbrand):
        if isinstance(element, str) and isinstance(negation, str):
            return element == negation
        elif isinstance(element, Formula) and isinstance(negation, Formula):
            if isinstance(element, Predicate) and isinstance(negation, Predicate):
                if len(element.args) != len(negation.args) or element.name != negation.name:
                    return False
            elif isinstance(element, Skolem) and isinstance(negation, Skolem):
                if element.skole_count != negation.skole_count:
                    return False
            for i in range(len(element.args)):
                if not _check_element(element.args[i], negation.args[i]):
                    return False
            return True
            # elif isinstance(element, Skolem) or isinstance(negation, Skolem):
            # return True
    elif isinstance(element, Herbrand):
        return False
    elif isinstance(negation, Herbrand):
        return False
    else:
        return False


def pretty_print(formula):
    """

    :param formula:
    :return:
    """
    if isinstance(formula, Symbol) or isinstance(formula, Predicate):
        text = str(formula)
    elif isinstance(formula, Not):
        text = "¬" + pretty_print(formula.args[0])
    else:
        temp = []
        for arg in formula.args:
            temp.append(pretty_print(arg))
        if isinstance(formula, And):
            text = " ∧ ".join(temp)
        elif isinstance(formula, Or):
            text = " ∨ ".join(temp)
        elif isinstance(formula, If):
            text = " → ".join(temp)
        elif isinstance(formula, Iff):
            text = " ↔ ".join(temp)
        else:
            raise TypeError("Invalid Formula Type: " + str(type(formula)))
        text = "(" + text + ")"
    return text.strip()
