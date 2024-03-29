from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register(identifier="A100702")
def buttered_croissant() -> "Iterable[int]":
    """Layers of dough separated by butter in successive foldings of croissant dough."""
    yield 1  # special case
    for n in count(start=1):  # pragma: no branch
        yield 1 + 2 * pow(3, n - 1)
