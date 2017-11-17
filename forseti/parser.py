"""
Parser for converting plain-text to Forseti formula
"""

from forseti.parsers.functional_parser import FunctionalParser
from forseti.formula import Formula

DEFAULT_PARSER = FunctionalParser
CURRENT_PARSER = None


def parse(statement):
    """
    Parse a plain-text string into Forseti formula

    TODO: raise exception on invalid formulas

    :param statement:
    :return: Predicate
    """
    if isinstance(statement, Formula):
        return statement
    elif statement is None or not isinstance(statement, str):
        raise TypeError("Statement cannot be " + str(type(statement)))
    if CURRENT_PARSER is None:
        return DEFAULT_PARSER.parse(statement, [])
    else:
        return CURRENT_PARSER.parse(statement, [])


if __name__ == "__main__":
    p = parse("forall(x,if(S(x),exists(y,and(S(y),forall(z,iff(B(z,y),and(B(z,x),B(z,z))))))))")
    print(p)
