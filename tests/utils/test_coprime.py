# coding=utf-8
import sys
from functools import reduce
from math import gcd

from hypothesis import given
from hypothesis.strategies import integers
from oeis.utils import coprime

if sys.version_info.major >= 3 and sys.version_info.minor >= 9:
    from math import lcm
else:

    def lcm(*integers) -> int:
        return reduce(lambda x, y: (x * y) / gcd(x, y), integers, 1)


@given(a=integers(min_value=2, max_value=100), b=integers(min_value=2, max_value=100))
def test_lcm_property(a: int, b: int) -> None:
    if coprime(a, b):
        assert lcm(a, b) == a * b
