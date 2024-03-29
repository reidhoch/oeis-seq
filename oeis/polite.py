from itertools import count
from math import floor, log2
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A138591")
def polite() -> "Iterable[int]":
    """Polite numbers."""
    for i in count(start=2):  # pragma: no branch
        yield i + floor(log2(i + log2(i)))
