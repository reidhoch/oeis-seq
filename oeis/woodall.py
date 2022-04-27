from itertools import count
from typing import Iterable

from .registry import registry


@registry.register("A003261")
def woodall() -> Iterable[int]:
    """Woodall (or Riesel) numbers."""
    for n in count(start=1):  # pragma: no branch
        yield n * (2**n) - 1
