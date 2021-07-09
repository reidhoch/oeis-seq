# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry


def centered_polygonal(k: int) -> Iterable[int]:
    """
    Centered polygonal numbers.

    Args:
            k: # of sides.
    """
    yield 1
    for n in count(start=1):
        yield ((k * n * (n + 1)) // 2) + 1


@registry.register("A005448")
def centered_triangular() -> Iterable[int]:
    """Centered triangular numbers."""
    return centered_polygonal(3)


@registry.register("A001844")
def centered_square() -> Iterable[int]:
    """Centered square numbers."""
    return centered_polygonal(4)


@registry.register("A005891")
def centered_pentagonal() -> Iterable[int]:
    """Centered pentagonal numbers."""
    return centered_polygonal(5)


@registry.register("A003215")
def centered_hexagonal() -> Iterable[int]:
    """Centered hexagonal numbers."""
    return centered_polygonal(6)
