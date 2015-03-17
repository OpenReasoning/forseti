"""
Predicate for use within Forseti
"""


class Predicate(object):
    """
    Base predicate class. All others should extend this.
    """
    def __init__(self, *kwargs):
        self.args = []
        self.name = ""
        self.type = None

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


class Atomic(Predicate):
    """
    Atomic predicates. Makes up base of other predicates
    """
    def __init__(self, arg):
        super(Atomic, self).__init__()
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
