from collections.abc import Iterable
from itertools import cycle

from oeis.registry import registry


@registry.register("A000035")
def period2() -> Iterable[int]:
    """Period 2: repeat [0, 1]."""
    return cycle([0, 1])
