"""
Parser for converting plain-text to Forseti Predicates
"""

from forseti.predicate import Atomic, Not, And, Or, Implies, Equiv


def parse(string):
    """
    Parse a plain-text string into Forseti implementation

    :param string:
    :return: Predicate
    """
    string = string.replace(" ", "")

    if len(string) == 0 or string == "()":
        return None

    while string[0] == "(" and string[-1] == ")":
        string = string[1:-1]

    if string.lower().startswith("and"):
        predicate = And
    elif string.lower().startswith("or"):
        predicate = Or
    elif string.lower().startswith("implies"):
        predicate = Implies
    elif string.lower().startswith("equiv"):
        predicate = Equiv
    elif string.lower().startswith("not"):
        predicate = Not
    else:
        predicate = Atomic
    return _parse_predicate(string, predicate)


def _parse_predicate(string, predicate):
    """
    Break the string into arguments to pass into the given predicate

    :param string:
    :param predicate:
    :return:
    """
    string = string[len(predicate.name):]
    if len(string) > 2 and string[0] == "(" and string[-1] == ")":
        string = string[1:-1]
        arg_list = []
        status = _get_arg_list(arg_list, string)
        if status is False or len(arg_list) != And.argument_number():
            return None

        # pylint: disable=star-args
        return predicate(*arg_list)
    elif predicate == Atomic:
        atomic = ""
        for char in string:
            if not char.isalnum():
                return None
            atomic += char

        return Atomic(atomic)

    else:
        return None


def _get_arg_list(arg_list, string):
    """
    get the argument list of a 2+ argument predicate

    :param arg_list:
    :param string:
    :return:
    """
    i = 0
    open_p = 0
    arg = ""
    while i < len(string):
        char = string[i]
        if char == "(":
            open_p += 1

        elif char == ")" and open_p >= 0:
            open_p -= 1

        if not char.isalnum() and (char != "," and open_p == 0):
            return False

        if (char == "," or char == ")") and open_p == 0:
            arg_list.append(parse(arg))
            arg = ""
        else:
            arg += char
        i += 1
    arg_list.append(parse(arg))
    return True
