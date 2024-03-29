from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000129")
def pell() -> "Iterable[int]":
    """Pell numbers."""
    yield 0  # pell(0)
    yield 1  # pell(1)
    p2: int = 0  # pell(0)
    p1: int = 1  # pell(1)
    while True:
        curr: int = (2 * p1) + p2
        yield curr
        p1, p2 = curr, p1
