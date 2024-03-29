from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000032")
def lucas() -> "Iterable[int]":
    """Lucas numbers."""
    yield 2  # special case
    yield 1  # special case
    prev: int = 2  # initially set to lucas(0)
    curr: int = 1  # initially set to lucas(1)
    while True:
        prev, curr = curr, prev + curr
        yield curr
