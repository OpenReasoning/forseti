"""
A brief demonstration of using the prover within Forseti
"""

from __future__ import print_function
from forseti.prover import Prover

# pylint: disable=duplicate-code
prover = Prover()
prover.add_formula("or(iff(G,H),iff(not(G),H))")
prover.add_goal("or(iff(not(G),not(H)),not(iff(G,H)))")
print(prover.run_prover())
print("\n".join(prover.get_proof()))


print("\n\n")

prover = Prover()
prover.add_formula("forall(x,if(S(x),exists(y,and(S(y),forall(z,iff(B(z,y),and(B(z,x),B(z,z))))))))")
prover.add_formula("forall(x,not(B(x,x)))")
prover.add_formula("exists(x,S(x))")
prover.add_goal("exists(x,and(S(x),forall(y,not(B(y,x)))))")
print(prover.run_prover())
print("\n".join(prover.get_proof()))
