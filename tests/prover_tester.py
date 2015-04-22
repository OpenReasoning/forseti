# pylint: disable=missing-docstring

from nose.tools import raises
from forseti.prover import Prover


@raises(TypeError)
def test_prover_formula_error():
    prover = Prover()
    prover.add_formula(None)


@raises(Exception)
def test_prover_no_goal_error():
    prover = Prover()
    prover.run_prover()
