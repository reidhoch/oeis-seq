from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A002378")
def oblong() -> "Iterable[int]":
    """Oblong (or promic, pronic, or heteromecic) numbers."""
    for n in count(start=0):  # pragma: no branch
        yield n * (n + 1)
