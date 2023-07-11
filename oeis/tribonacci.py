from typing import TYPE_CHECKING

from .registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000073")
def tribonacci() -> "Iterable[int]":
    """Tribonacci numbers."""
    yield 0
    yield 0
    yield 1
    p3: int = 0  # tribonacci(0)
    p2: int = 0  # tribonacci(1)
    p1: int = 1  # tribonacci(2)
    while True:
        curr: int = p1 + p2 + p3
        yield curr
        p1, p2, p3 = curr, p1, p2
