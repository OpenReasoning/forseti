"""
Automated Theorem Prover within Forseti
"""
# pylint: disable=fixme
from __future__ import print_function
from copy import deepcopy
from forseti.formula import Not, And, Or
from forseti import converter, parser
import forseti.util as util


class Prover(object):
    """
    Prover class
    """
    def __init__(self):
        self._cnf_list = []
        self.formulas = []
        self.goals = []
        self._goals = []

    def add_formula(self, statement):
        """

        :param statement:
        :return:
        """
        if isinstance(statement, str):
            statement = parser.parse(statement)
        self._add_statement(deepcopy(statement), self.formulas)

    def add_goal(self, statement):
        """

        :param statement:
        :return:
        """
        statement = parser.parse(statement)
        self._add_statement(deepcopy(statement), self.goals)
        self._add_statement(Not(deepcopy(statement)), self._goals)

    @staticmethod
    def _add_statement(statement, add_to_list):
        """

        :param statement:
        :param add_to_list:
        :param additional: additional operator to apply onto statement
        :return:
        """
        statement = parser.parse(statement)
        statement = converter.convert_to_cnf(statement)
        add_to_list.append(statement)

    def run_prover(self):
        """

        :return:
        """
        if len(self.goals) == 0:
            # TODO: give this a better exception class
            raise Exception("You need at least one goal!")

        for formula in self.formulas:
            converts = self._convert_formula(formula)
            for convert in converts:
                self._cnf_list += [convert]
        for goal in self._goals:
            converts = self._convert_formula(goal)
            for convert in converts:
                self._cnf_list += [convert]

        self._tautology_elimination()
        for i in range(len(self._cnf_list)):
            self._cnf_list[i] = sorted(self._cnf_list[i])
        return self._resolve()

    @staticmethod
    def _convert_formula(formula):
        """
        Converts a CNF formula into lists for resolution.
        Ex:
        and(a,b) -> [[a], [b]]
        or(a,b) -> [[a,b]]
        and(or(a,b),c) -> [[a,b],[c]]

        :type formula: LogicalOperator or Symbol
        """
        cnf_list = [[formula]]
        all_checked = False
        break_from = False
        while not all_checked:
            all_checked = True
            for i in range(len(cnf_list)):
                for j in range(len(cnf_list[i])):
                    statement = cnf_list[i][j]
                    if isinstance(statement, And) or isinstance(statement, Or):
                        if isinstance(statement, And):
                            cnf_list.insert(i + 1, [statement.args[0]])
                            cnf_list.insert(i + 2, [statement.args[1]])
                        elif isinstance(statement, Or):
                            cnf_list[i].insert(j + 1, statement.args[0])
                            cnf_list[i].insert(j + 2, statement.args[1])

                        cnf_list[i].pop(j)
                        if len(cnf_list[i]) == 0:
                            cnf_list.pop(i)
                        break_from = True
                        all_checked = False
                        break
                if break_from is True:
                    break_from = False
                    break
        return cnf_list

    def _resolve(self):
        """

        :return:
        """
        i = 0
        checked = list()
        while i < len(self._cnf_list):
            j = i + 1
            while j < len(self._cnf_list):
                if [i, j] in checked:
                    j += 1
                    continue
                checked.append([i, j])
                have_resolve = False
                for k in range(len(self._cnf_list[i])):
                    atomic = self._cnf_list[i][k]
                    negation = util.negate_formula(atomic)
                    try:
                        ind = self._cnf_list[j].index(negation)
                        new_cnf = self._cnf_list[i][:k]
                        new_cnf += self._cnf_list[i][(k+1):]
                        for cnf in self._cnf_list[j][:ind]:
                            if cnf not in new_cnf:
                                new_cnf.append(cnf)
                        for cnf in self._cnf_list[j][(ind+1):]:
                            if cnf not in new_cnf:
                                new_cnf.append(cnf)
                        new_cnf.sort()
                        if len(new_cnf) == 0:
                            return True
                        if not util.is_tautology(new_cnf) and \
                           new_cnf not in self._cnf_list:
                            have_resolve = True
                            self._cnf_list.append(new_cnf)
                            checked.append([i, len(self._cnf_list)-1])
                            checked.append([j, len(self._cnf_list)-1])
                    except ValueError:
                        pass
                if have_resolve is True:
                    i = -1
                    break
                j += 1
            i += 1
        return False

    def _tautology_elimination(self):
        """

        :return:
        """
        i = 0
        while i < len(self._cnf_list):
            cnf = self._cnf_list[i]
            if util.is_tautology(cnf):
                self._cnf_list.pop(i)
                i -= 1
            i += 1
