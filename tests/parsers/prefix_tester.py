# pylint: disable=missing-docstring

from __future__ import unicode_literals
from forseti import parser
from forseti.parsers.prefix_parser import PrefixParser
from forseti.formula import Predicate, Skolem, Herbrand


def setup():
    Predicate.reset()
    Skolem.reset()
    Herbrand.reset()


def setup_class():
    parser.CURRENT_PARSER = Prefix


def test_parse_symbol():
    parser.parse("A")