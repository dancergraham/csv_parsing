import unittest
from nose.tools import assert_almost_equal
from lib.compute import compute_u_from_delta_p


class TestCompute(unittest.TestCase):
    def test_compute_u(self):
        test_cases = [(0, 1.225, 0), (1, 1.225, 1.27775),
                      (2.432, 1.225, 1.99264), (4267.42, 1.225, 83.46985), ("234", 1.225, 19.54586)]
        for (value_to_test, rho, expected_computation_result) in test_cases:
            print(compute_u_from_delta_p(value_to_test, rho),
                  expected_computation_result)
            assert_almost_equal(
                compute_u_from_delta_p(value_to_test, rho), expected_computation_result, places=5)
