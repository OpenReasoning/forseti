# -*- coding: utf-8 -*-
"""
Predicate for use within Forseti
"""
# pylint: disable=too-few-public-methods,missing-docstring


class Formula(object):
    args = []

    def __init__(self):
        pass

    def __repr__(self):
        raise NotImplementedError("Not implemented")

    def __str__(self):
        raise NotImplementedError("Not implemented")

    def __eq__(self, other):
        raise NotImplementedError("Not implemented")

    def __ne__(self, other):
        raise NotImplementedError("Not implemented")

    def __lt__(self, other):
        raise NotImplementedError("Not implemented")

    def __le__(self, other):
        raise NotImplementedError("Not implemented")

    def __gt__(self, other):
        raise NotImplementedError("Not implemented")

    def __ge__(self, other):
        raise NotImplementedError("Not implemented")


class Symbol(Formula):
    """
    Symbols, smallest logical unit. Only accepts strings to label them
    """
    name = "Symbol"
    arity = 0

    def __init__(self, arg):
        if not isinstance(arg, str):
            raise TypeError(str(arg) + " is not a string type")
        super(Symbol, self).__init__()
        self.arg = arg
        self. args = [arg]

    def __repr__(self):
        """
        see __repr__()
        """
        return self.arg

    def __str__(self):
        return self.arg

    def __eq__(self, other):
        """
        Test if a symbol is equal with another symbol (otherwise False)
        """
        if isinstance(other, Symbol):
            return self.arg == other.arg
        else:
            return False

    def __ne__(self, other):
        """
        Test if symbol is not equal with another symbol (otherwise True)
        """
        return not self == other

    def __lt__(self, other):
        if isinstance(other, Symbol):
            return self.arg < other.arg
        else:
            return True

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other < self or other == self


class LogicalOperator(Formula):
    """
    Base LogicalOperator class. LogicalOperators are "Not", "Or", etc that
    take in true/false values and would return a true/false value
    """
    name = ""
    arity = 0

    def __init__(self, *kwargs):
        """

        :type kwargs: list (LogicalOperator | Symbol)
        """
        super(LogicalOperator, self).__init__()
        self.args = []
        # kwargs = sorted(kwargs)
        for kwarg in kwargs:
            if not isinstance(kwarg, Formula):
                raise TypeError(str(kwarg) + " is not an Operator or Symbol")

    def get_arity(self):
        return self.arity

    def __repr__(self):
        """
        Return __repr__() for predicate

        :return: __repr__()
        """
        raise NotImplementedError("Not implemented")

    def __str__(self):
        raise NotImplementedError("Not implemented")

    def __eq__(self, other):
        if isinstance(self, type(other)):
            if self.arity == other.arity:
                for i in range(self.arity):
                    if self.args[i] != other.args[i]:
                        return False
                return True
        return False

    def __ne__(self, other):
        return not self == other

    """
    Not < And < Or < If < Iff
    """
    def __lt__(self, other):
        if isinstance(other, Symbol):
            return False
        else:
            if isinstance(self, type(other)):
                for i in range(self.arity):
                    if not self.args[i] < other.args[i]:
                        return False
                return True
            elif isinstance(self, Not):
                return True
            elif isinstance(self, And):
                if isinstance(other, Not):
                    return False
                else:
                    return True
            elif isinstance(self, Or):
                if isinstance(other, Not) or isinstance(other, And):
                    return False
                else:
                    return True
            elif isinstance(self, If):
                if not isinstance(other, Iff):
                    return True
                else:
                    return False
            return False

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other < self or other == self


class Not(LogicalOperator):
    """
    Not (negation) Predicate
    """
    name = "not"
    arity = 1

    def __init__(self, arg):
        super(Not, self).__init__(arg)
        self.args.append(arg)

    def __repr__(self):
        return "not("+self.args[0].__repr__()+")"

    def __str__(self):
        return "~"+self.args[0].__str__()


class And(LogicalOperator):
    """
    And Predicate
    """
    name = "and"
    arity = 2

    def __init__(self, arg1, arg2):
        super(And, self).__init__(arg1, arg2)
        self.args.append(arg1)
        self.args.append(arg2)

    def __repr__(self):
        return "and(" + self.args[0].__repr__() + ", " + \
               self.args[1].__repr__() + ")"

    def __str__(self):
        return "(" + self.args[0].__str__() + " & " + \
               self.args[1].__str__() + ")"


class Or(LogicalOperator):
    """
    Or Predicate
    """
    name = "or"
    arity = 2

    def __init__(self, arg1, arg2):
        super(Or, self).__init__(arg1, arg2)
        self.args.append(arg1)
        self.args.append(arg2)

    def __repr__(self):
        return "or(" + self.args[0].__repr__() + ", " \
               + self.args[1].__repr__() + ")"

    def __str__(self):
        return "(" + self.args[0].__str__() + " | " \
               + self.args[1].__str__() + ")"


class If(LogicalOperator):
    """
    Implies (Material Conditional) Predicate
    """
    name = "if"
    arity = 2

    def __init__(self, arg1, arg2):
        super(If, self).__init__(arg1, arg2)
        self.args.append(arg1)
        self.args.append(arg2)

    def __repr__(self):
        return "if(" + self.args[0].__repr__() + ", " \
               + self.args[1].__repr__() + ")"

    def __str__(self):
        return "(" + self.args[0].__str__() + " -> " \
               + self.args[1].__str__() + ")"


class Iff(LogicalOperator):
    """
    Equiv(alence) Predicate
    """
    name = "iff"
    arity = 2

    def __init__(self, arg1, arg2):
        super(Iff, self).__init__(arg1, arg2)
        self.args.append(arg1)
        self.args.append(arg2)

    def __repr__(self):
        return "iff(" + self.args[0].__repr__() + ", " \
               + self.args[1].__repr__() + ")"

    def __str__(self):
        return "(" + self.args[0].__str__() + " <-> " \
               + self.args[1].__str__() + ")"


class Predicate(Formula):
    """
    User defined predicates
    """
    defined = {}

    def __init__(self, name, args):
        super(Predicate, self).__init__()
        if name in Predicate.defined and len(args) != Predicate.defined[name]['arity']:
            # TODO: throw better exception?
            raise Exception
        Predicate.defined[name] = {"name": name, "arity": len(args)}
        self.name = name
        self.args = args
        self.arity = len(args)

    @staticmethod
    def get_arity(type_name):
        if type_name in Predicate.defined:
            return Predicate.defined[type_name]['arity']
        else:
            return -1

    @staticmethod
    def reset():
        Predicate.defined = {}

    def __repr__(self):
        return self.name+"(" + ", ".join([str(x) for x in self.args]) + ")"

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(self, type(other)):
            if self.name == other.name and self.arity == other.arity:
                for i in range(self.arity):
                    if self.args[i] != other.args[i]:
                        return False
                return True
        return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return NotImplemented


class Quantifier(Formula):
    """
    Implementation of Quantifier for formulas
    """
    def __init__(self, arg1, arg2):
        super(Quantifier, self).__init__()
        if isinstance(arg1, Symbol):
            self.symbol = arg1.arg
        elif isinstance(arg1, str):
            self.symbol = arg1
        else:
            raise Exception

        self.args = [arg2]

    def __repr__(self):
        raise NotImplementedError("Not implemented")

    def __str__(self):
        raise NotImplementedError("Not implemented")

    def __eq__(self, other):
        if isinstance(self, type(other)):
            if self.symbol == other.symbol:
                return self.args[0] == other.args[0]
        return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Quantifier):
            return False


class Universal(Quantifier):
    """
    Implementation of Universal Quantifier
    """
    name = "forall"
    arity = 2

    def __init__(self, arg1, arg2):
        super(Universal, self).__init__(arg1, arg2)

    def __repr__(self):
        return "forall([" + self.symbol + "], " + repr(self.args[0]) + ")"

    def __str__(self):
        return u"∀" + self.symbol + "(" + str(self.args[0]) + ")"


class Existential(Quantifier):
    """
    Implementation of Existential Quantifier
    """
    name = "exists"
    arity = 2

    def __init__(self, arg1, arg2):
        super(Existential, self).__init__(arg1, arg2)

    def __repr__(self):
        return "exists([" + self.symbol + "], " + repr(self.args[0]) + ")"

    def __str__(self):
        return u"∃" + self.symbol + "(" + str(self.args[0]) + ")"


class Skolem(Formula):
    count = 1
    args = []

    def __init__(self):
        super(Skolem, self).__init__()
        self.skole_count = Skolem.count
        Skolem.count += 1

    def __repr__(self):
        return "Skolem" + str(self.skole_count)

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        return isinstance(self, type(other)) and self.skole_count == other.skole_count

    def __ne__(self, other):
        return not self == other

    @staticmethod
    def reset():
        Skolem.count = 1


class Herbrand(Formula):
    count = 1
    args = []

    def __init__(self):
        super(Herbrand, self).__init__()
        self.herbrand_count = Herbrand.count
        Herbrand.count += 1

    def __repr__(self):
        return "Herbrand" + str(self.herbrand_count)

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        if isinstance(self, Herbrand) and isinstance(other, Herbrand):
            return self.herbrand_count == other.herbrand_count
        else:
            return True

    def __ne__(self, other):
        return not self == other

    @staticmethod
    def reset():
        Herbrand.count = 1


class FrozenFormula(object):
    def __init__(self, formula):
        self.formula = formula

    def __hash__(self):
        return hash(repr(self))