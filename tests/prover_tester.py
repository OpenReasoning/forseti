# pylint: disable=missing-docstring

from __future__ import unicode_literals
from nose.tools import assert_equal, raises
from forseti.prover import Prover


def test_get_proof():
    prover = Prover()
    prover.add_formula("and(a,b)")
    prover.add_goal("a")
    prover.run_prover()
    proof = prover.get_proof()
    expected = ['  1)    a                                                    '
                '                    Assumption',
                '  3)    ~a                                                   '
                '                    Assumption',
                '  4)    $$FALSE                                              '
                '                    resolve(1,3)']
    assert_equal(expected, proof)


@raises(TypeError)
def test_prover_formula_error():
    prover = Prover()
    prover.add_formula(None)


@raises(Exception)
def test_prover_no_goal_error():
    prover = Prover()
    prover.run_prover()
