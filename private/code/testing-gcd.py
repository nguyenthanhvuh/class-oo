from parameterized import parameterized
import unittest

def gcd_correct(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def gcd_buggy(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class TestGCD(unittest.TestCase):

    @parameterized.expand([
        (6, 9),
        (9, 6),
        (0, 15),
        (15, 0),
        (-6, 9),
        (6, -9),
        (-6, -9),
        (0, 0),
        (20, 100),
        (-20, -100),
    ])
    def test_gcds(self, a, b):
        expected = gcd_correct(a, b)
        actual = gcd_buggy(a, b)
        self.assertEqual(expected, actual, 
                         f"Buggy failed on ({a}, {b}): expected {expected}, got {actual}")



from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=-1000, max_value=1000), integers(min_value=-1000, max_value=1000))
def test_property_non_negative(a, b):
    assert gcd_correct(a, b) >= 0
    assert gcd_buggy(a, b) >= 0, (a,b)  # This will FAIL for some inputs!
    
    
    
if __name__ == '__main__':
    #unittest.main()
    test_property_non_negative()