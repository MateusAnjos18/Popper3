import numpy as np

def test_gravity_acceleration():
    g = 9.81  # m/s²
    t = 2.0   # s
    s = 0.5 * g * t**2
    assert np.isclose(s, 19.62)
