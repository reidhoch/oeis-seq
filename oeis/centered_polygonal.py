# coding=utf-8
from typing import Iterable
from itertools import count
from oeis.registry import registry


def centered_polygonal(k: int) -> Iterable[int]:
    yield 1
    for n in count(start=1):
        yield ((k * n * (n + 1)) // 2) + 1


@registry.register("A005448")
def centered_triangular() -> Iterable[int]:
    return centered_polygonal(3)


@registry.register("A001844")
def centered_square() -> Iterable[int]:
    return centered_polygonal(4)
