from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry
from oeis.utils import is_prime

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A002808")
def composite() -> "Iterable[int]":
    """Composite numbers."""
    for n in count(start=4):  # pragma: no branch
        if not is_prime(n):
            yield n
