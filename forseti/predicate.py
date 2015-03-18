"""
Predicate for use within Forseti
"""


class Predicate(object):
    """
    Base predicate class. All others should extend this.
    """
    def __init__(self, *kwargs):
        self.args = []

        for kwarg in kwargs:
            if not isinstance(kwarg, Predicate):
                raise TypeError(str(kwarg) + " is not a Predicate")

    @staticmethod
    def argument_number():
        """
        Number of arguments that the predicate requires

        :return int: number of arguments
        """
        raise NotImplementedError("Not implemented yet")

    def get_print(self):
        """
        Return string representation of predicate for printing

        :return string: string representation
        """
        raise NotImplementedError("Not implemented yet")

    def get_pretty_print(self):
        """
        Return string representation that's more human readable for predicate

        :return string: string representation
        """
        raise NotImplementedError("Not implemented yet")

    def __str__(self):
        """
        Return get_print() for predicate

        :return: get_print()
        """
        return self.get_print()

    def __eq__(self, other):
        if type(self) == type(other):
            if self.argument_number() == other.argument_number():
                for i in range(self.argument_number()):
                    if self.args[i] != other.args[i]:
                        return False
        return True

    def __ne__(self, other):
        return not self == other


class Atomic(Predicate):
    """
    Atomic predicates. Makes up base of other predicates
    """
    name = ""

    def __init__(self, arg):
        super(Atomic, self).__init__()
        if type(arg) != str:
            raise TypeError(str(arg) + " is not a string/atomic")
        self.args.append(arg)

    @staticmethod
    def argument_number():
        return 1

    def get_print(self):
        return self.args[0]

    def get_pretty_print(self):
        return self.args[0]


class Not(Predicate):
    """
    Not (negation) Predicate
    """
    name = "not"

    def __init__(self, arg):
        super(Not, self).__init__(arg)
        self.args.append(arg)

    @staticmethod
    def argument_number():
        return 1

    def get_print(self):
        return "not("+self.args[0].get_print()+")"

    def get_pretty_print(self):
        return "~"+self.args[0].get_pretty_print()


class And(Predicate):
    """
    And Predicate
    """
    name = "and"

    def __init__(self, arg1, arg2):
        super(And, self).__init__(arg1, arg2)
        self.args.append(arg1)
        self.args.append(arg2)

    @staticmethod
    def argument_number():
        return 2

    def get_print(self):
        return "and(" + self.args[0].get_print() + ", " + \
               self.args[1].get_print() + ")"

    def get_pretty_print(self):
        return "(" + self.args[0].get_pretty_print() + " & " + \
               self.args[1].get_pretty_print() + ")"


class Or(Predicate):
    """
    Or Predicate
    """
    name = "or"

    def __init__(self, arg1, arg2):
        super(Or, self).__init__(arg1, arg2)
        self.args.append(arg1)
        self.args.append(arg2)

    @staticmethod
    def argument_number():
        return 2

    def get_print(self):
        return "or(" + self.args[0].get_print() + ", " \
               + self.args[1].get_print() + ")"

    def get_pretty_print(self):
        return "(" + self.args[0].get_pretty_print() + " | " \
               + self.args[1].get_pretty_print() + ")"


class Implies(Predicate):
    """
    Implies (Material Conditional) Predicate
    """
    name = "implies"

    def __init__(self, arg1, arg2):
        super(Implies, self).__init__(arg1, arg2)
        self.args.append(arg1)
        self.args.append(arg2)

    @staticmethod
    def argument_number():
        return 2

    def get_print(self):
        return "implies(" + self.args[0].get_print() + ", " \
               + self.args[1].get_print() + ")"

    def get_pretty_print(self):
        return "(" + self.args[0].get_pretty_print() + " -> " \
               + self.args[1].get_pretty_print() + ")"


class Equiv(Predicate):
    """
    Equiv(alence) Predicate
    """
    name = "equiv"

    def __init__(self, arg1, arg2):
        super(Equiv, self).__init__(arg1, arg2)
        self.args.append(arg1)
        self.args.append(arg2)

    @staticmethod
    def argument_number():
        return 2

    def get_print(self):
        return "equiv(" + self.args[0].get_print() + ", " \
               + self.args[1].get_print() + ")"

    def get_pretty_print(self):
        return "(" + self.args[0].get_pretty_print() + " <-> " \
               + self.args[1].get_pretty_print() + ")"
