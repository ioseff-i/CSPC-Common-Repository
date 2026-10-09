import pytest
import numpy as np
import decay

def test_decay_initial():
    res = decay.simulate(1000, 0.4)
    assert res[0] == 1000

def test_negative_rate_raises_value_error():
    with pytest.raises(ValueError):
        decay.simulate(1000, -0.4)

def test_simulation_average_theoretical():
    N0 = 10000
    rate = 0.4
    t_final = 10.0  # Adjust if decay.py uses a different t_max
    results = [decay.simulate(N0, rate)[-1] for _ in range(100)]
    avg = np.mean(results)
    expected = N0 * np.exp(-rate * t_final)
    assert avg == pytest.approx(expected, rel=0.15)
