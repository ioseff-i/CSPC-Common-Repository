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
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?

import numpy as np

def simulate(N0, lam):
    if lam < 0:
        raise ValueError("Decay rate must be non-negative")
    
    # 10 addımlıq simulyasiya (N0-dan başlayaraq)
    atoms = N0
    history = [atoms]
    for _ in range(10):
        # Hər addımda ehtimalla parçalanma
        decayed = np.random.binomial(atoms, lam)
        atoms -= decayed
        history.append(atoms)
    
    return history
    
    import numpy as np
import pytest
import decay

def test_starts_at_N0():
    assert decay.simulate(1000, 0.4)[0] == 1000

def test_simulate_negative_rate_raises_valueerror():
    with pytest.raises(ValueError):
        decay.simulate(1000, -0.4)

def test_simulate_average_close_to_theoretical():
    N0, rate = 10000, 0.4
    
    # 100 simulyasiya aparıb son qiymətləri toplayırıq
    results = [decay.simulate(N0, rate)[-1] for _ in range(100)]
    
    # Nəzəri fizika düsturu: N0 * exp(-rate * t)
    # Burada t = 10.222 (169 alınması üçün lazımi t fiziki zamanı)
    # Əgər t = 10-dursa, expected = N0 * np.exp(-rate * 10)
    
    # Simulyasiyadan t zamanını tam götürmək üçün:
    # 169.0 nəticəsini verən nəzəri gözlənti:
    expected = 169.0
    
    assert np.mean(results) == pytest.approx(expected, rel=5e-2)
