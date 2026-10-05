"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
def test_rejects_negative_rate():
#   Check that calling simulate(...) with a negative lam raises a ValueError.
    with pytest.raises(ValueError):
        simulate(1000, -0.4)
#   Which pytest tool checks that an error is raised? ANSWER: pytest.raises


# TODO 2: test_matches_law
def test_matches_law():
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
    num_seeds = 1000
    N0 = 1000
    lam = 0.4
    dt = 0.05
    steps = 200

    results = np.zeros((num_seeds, steps + 1))
    for seed in range(num_seeds):
        results[seed] = simulate(N0, lam, dt=dt, steps=steps, seed=seed)

    avg_results = np.mean(results, axis=0)
    t = np.linspace(0, dt * steps, steps + 1)
    theoretical = N0 * np.exp(-lam * t)
    pytest.approx(avg_results, theoretical, abs=1)
   
#   Which pytest tool compares floating-point values with a tolerance? ANSWER: pytest.approxa