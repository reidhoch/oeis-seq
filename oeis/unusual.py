from itertools import count
from math import sqrt
from typing import TYPE_CHECKING

from oeis.registry import registry

from .utils import prime_factors

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A064052")
def unusual() -> "Iterable[int]":
    """Unusual numbers, aka non-sqrt(n)-rough numbers."""
    for n in count(start=2):  # pragma: no branch
        factors: list[int] = prime_factors(n)
        gpf: int = max(factors)
        if gpf > sqrt(n):
            yield n
