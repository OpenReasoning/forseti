"""
Predicate for use within Forseti
"""
# pylint: disable=too-few-public-methods

class Symbol(object):
    """
    Symbols, smallest logical unit. Only accepts strings to label them
    """
    name = "Symbol"
    arity = 0

    def __init__(self, arg):
        if not isinstance(arg, str):
            raise TypeError(str(arg) + " is not a string")
        self.arg = arg
        self. args = [arg]

    def __str__(self):
        return self.arg

    def __repr__(self):
        """
        see __repr__()
        """
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
        if isinstance(other, LogicalOperator):
            return True
        elif isinstance(other, Symbol):
            return self.arg < other.arg
        else:
            return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other < self or other == self


class LogicalOperator(object):
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
        self.args = []
        kwargs = sorted(kwargs)
        for kwarg in kwargs:
            if not isinstance(kwarg, LogicalOperator) and not isinstance(kwarg, Symbol):
                raise TypeError(str(kwarg) + " is not an Operator or Symbol")

    def __str__(self):
        raise NotImplementedError("Not implemented yet")

    def __repr__(self):
        """
        Return __repr__() for predicate

        :return: __repr__()
        """
        raise NotImplementedError("Not implemented yet")

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

    def __lt__(self, other):
        if isinstance(other, Symbol):
            return False
        elif isinstance(other, LogicalOperator):
            if isinstance(self, type(other)):
                for i in range(self.arity):
                    if not self.args[i] < other.args[i]:
                        return False
                return True
        else:
            return NotImplemented

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
