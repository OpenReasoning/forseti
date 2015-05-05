"""
Test basic Predicate Calculus
"""
# pylint: disable=missing-docstring

from nose.tools import assert_true, with_setup
from forseti.prover import Prover
from forseti.formula import Predicate, Skolem, Herbrand


def setup():
    Predicate.reset()
    Herbrand.reset()
    Skolem.reset()


@with_setup(setup)
def test_pred_logic_1():
    prover = Prover()
    prover.add_formula("and(P(a),P(F(a,b)))")
    prover.add_goal("P(a)")
    assert_true(prover.run_prover())
