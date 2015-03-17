#pylint: skip-file
__author__ = 'mpeveler'

from forseti.predicate import *


def gen_formula(string):
    if len(string) == 0 or string == "()":
        return None

    if string[0] == "(" and string[-1] == ")":
        string = string[1:-1]

    arg_list = []
    if "and" == string[:3].lower():
        string = string[3:]
        if string[0] == "(" and string[-1] == ")":
            string = string[1:-1]
            arg = ""
            i = 0
            open_p = 0
            while i < range(len(string)):
                char = string[i]
                if char == "(":
                    open_p += 1
                    continue
                elif char == ")" and open_p > 0:
                    open_p -= 1
                if open_p < 0:
                    return None

                if not char.isalnum() and (char != "," and open_p == 0):
                    return None

                if (char == "," or char == ")") and open_p == 0:
                    arg_list.append(gen_formula(arg))
                    arg = ""
                else:
                    arg += char
                i += 1
            if i != len(string) or len(arg_list) != And.argument_number():
                return None
            return And(*arg_list)

        else:
            return None
    elif "or":
        pass
    elif "implies":
        pass
    elif "equiv":
        pass
    elif "not":
        pass
    else:
        atomic = ""
        for char in string:
            if not char.isalpha():
                return None
            atomic += char
        return Atomic(atomic)