"""
Automated Theorem Prover within Forseti
"""
# pylint: disable=fixme
from copy import deepcopy
import time

from forseti.formula import Formula, Not, And, Or, Skolem, Herbrand, Predicate
from forseti import converter, parser
import forseti.util as util
from forseti import exceptions


class Prover(object):
    """
    Prover class
    """

    def __init__(self, timeout=30):
        self._cnf_list = []
        self.parents = []
        self.formulas = []
        self.goals = []
        self._goals = []
        self.proof_found = False
        self.proof_time = 0
        self.proof_timeout = timeout

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
        statement = converter.convert_formula(statement)
        add_to_list.append(statement)

    def run_prover(self):
        """

        :return:
        """
        self.parents = []
        self.proof_found = False

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
        for i in range(len(self._cnf_list)):
            self.parents.append([])
        self.proof_found, self.proof_time = self._resolve()
        return self.proof_found

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
        for i in range(len(cnf_list)):
            j = 0
            while j < len(cnf_list[i]):
                if cnf_list[i][j] in cnf_list[i][j + 1:]:
                    cnf_list[i].pop(j)
                    j -= 1
                j += 1
        return cnf_list

    def _resolve(self):
        """

        :return:
        """
        start_time = time.time()
        i = 0
        checked = list()
        while i < len(self._cnf_list):
            if (time.time() - start_time) > self.proof_timeout:
                raise exceptions.TimeoutException('Proof timeout reached')
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
                        resolve = Prover._get_index(self._cnf_list[j], negation)
                        cnf_list1 = deepcopy(self._cnf_list[i])
                        cnf_list2 = deepcopy(self._cnf_list[j])
                        if resolve[1] >= 1:
                            Prover._remove_herbrand(resolve, cnf_list1, cnf_list2, k)
                        ind = resolve[0]
                        new_cnf = cnf_list1[:k]
                        new_cnf += cnf_list1[(k + 1):]
                        for cnf in cnf_list2[:ind]:
                            if cnf not in new_cnf:
                                new_cnf.append(cnf)
                        for cnf in cnf_list2[(ind + 1):]:
                            if cnf not in new_cnf:
                                new_cnf.append(cnf)
                        new_cnf.sort()
                        if len(new_cnf) == 0:
                            self._cnf_list.append([])
                            self.parents.append([i, j])
                            return True, time.time() - start_time
                        if not util.is_tautology(new_cnf) and \
                           new_cnf not in self._cnf_list:
                            have_resolve = True
                            self._cnf_list.append(new_cnf)
                            self.parents.append([i, j])
                            checked.append([i, len(self._cnf_list) - 1])
                            checked.append([j, len(self._cnf_list) - 1])
                    except ValueError:
                        pass
                if have_resolve is True:
                    i = -1
                    break
                j += 1
            i += 1
        return False, time.time() - start_time

    def _tautology_elimination(self):
        """
        Remove any CNF tautologies

        :return:
        """
        i = 0
        while i < len(self._cnf_list):
            cnf = self._cnf_list[i]
            if util.is_tautology(cnf):
                self._cnf_list.pop(i)
                i -= 1
            i += 1

    @staticmethod
    def _get_index(cnf_list, negation):
        for i in range(len(cnf_list)):
            element = cnf_list[i]
            run = Prover._check_element(element, negation, [False, 0, None, None])
            if run[0] is True:
                return [i, run[1], run[2], run[3]]
        raise ValueError

    @staticmethod
    def _check_element(element, negation, unify):
        if isinstance(element, type(negation)) and not isinstance(element, Herbrand):
            if isinstance(element, str) and isinstance(negation, str):
                return [element == negation, 0, None]
            elif isinstance(element, Formula) and isinstance(negation, Formula):
                if isinstance(element, Predicate) and isinstance(negation, Predicate):
                    if len(element.args) != len(negation.args) or element.name != negation.name:
                        return [False, 0, None, None]
                elif isinstance(element, Skolem) and isinstance(negation, Skolem):
                    if element.skole_count != negation.skole_count:
                        return [False, 0, None, None]
                ret = [True, 0, None, None]
                for i in range(len(element.args)):
                    r = Prover._check_element(element.args[i], negation.args[i], ret)
                    if r[0] is True and r[1] > 0:
                        ret = [True, r[1], r[2], r[3]]
                    elif not r[0]:
                        return [False, 0, None, None]
                return ret
            # elif isinstance(element, Skolem) or isinstance(negation, Skolem):
            #            return True
        elif isinstance(element, Herbrand):
            if unify[1] == 2:
                return [False, 0, None, None]
            elif unify[1] == 1 and (unify[2] != element or unify[3] != negation):
                return [False, 0, None, None]
            return [True, 1, deepcopy(element), deepcopy(negation)]
        elif isinstance(negation, Herbrand):
            if unify[1] == 1:
                return [False, 0, None, None]
            elif unify[1] == 2 and (unify[2] != element or unify[3] != negation):
                return [False, 0, None, None]
            return [True, 2, deepcopy(element), deepcopy(negation)]
        else:
            return [False, 0, None, None]

    @staticmethod
    def _remove_herbrand(resolve, cnf_list1, cnf_list2, k):
        if resolve[1] == 2:
            assert isinstance(resolve[3], Herbrand)
            for elem in range(len(cnf_list1)):
                if elem == k:
                    continue

                cnf_list1[elem] = Prover._replace_herbrand(
                    cnf_list1[elem], resolve[3], resolve[2])
        elif resolve[1] == 1:
            assert isinstance(resolve[2], Herbrand)
            for elem in range(len(cnf_list2)):
                cnf_list2[elem] = Prover._replace_herbrand(
                    cnf_list2[elem], resolve[2], resolve[3])

    @staticmethod
    def _replace_herbrand(element, replace, replacement):
        if isinstance(element, str):
            return element
        assert isinstance(element, Formula)
        assert isinstance(replace, Herbrand)
        assert isinstance(replacement, Formula)
        if isinstance(element, Herbrand):
            if replace.herbrand_count == element.herbrand_count:
                element = deepcopy(replacement)
        for i in range(len(element.args)):
            if isinstance(element.args[i], Herbrand):
                if replace.herbrand_count == element.args[i].herbrand_count:
                    element.args[i] = deepcopy(replacement)
            else:
                element.args[i] = Prover._replace_herbrand(element.args[i],
                                                           replace,
                                                           replacement)
        return element

    def get_proof(self):
        if self.proof_found is False:
            return ["No Proof"]
        proof = []
        proof_parents = [self.parents[-1]]
        proof_formulas = {len(self.parents) - 1}
        while True:
            if len(proof_parents) > 0:
                x = proof_parents.pop(0)
                for i in x:
                    proof_parents.append(self.parents[i])
                    proof_formulas.add(i)
            else:
                break

        proof_formulas = sorted(proof_formulas)
        for i in proof_formulas:
            extra = "Assumption"
            if len(self.parents[i]) > 0:
                extra = "resolve(" + ",".join([str(y+1) for y in self.parents[i]]) + ")"
            cnf = str(util.cnf_list_as_disjunction(self._cnf_list[i]))
            proof.append(((str(i+1) + ")").rjust(4) + "    " + cnf.ljust(70) + "   " + extra))
        return proof


if __name__ == "__main__":
    prover = Prover()
    prover.add_formula("exists(x,forall(y,A(x,y)))")
    prover.add_goal("exists(x,A(x,a))")
    print(prover.run_prover())
    print("\n".join(prover.get_proof()))
