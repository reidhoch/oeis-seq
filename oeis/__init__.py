# coding=utf-8
"""OEIS Sequences."""
from .abundant import abundant
from .arithmetic import arithmetic
from .buttered_croissant import buttered_croissant
from .catalan import catalan
from .centered_polygonal import (
    centered_decagonal,
    centered_dodecagonal,
    centered_hendecagonal,
    centered_heptagonal,
    centered_hexagonal,
    centered_nonagonal,
    centered_octagonal,
    centered_pentagonal,
    centered_polygonal,
    centered_square,
    centered_triangular,
)
from .composite import composite
from .deficient import deficient
from .eratosthenes import eratosthenes
from .factorial import factorial
from .fibonacci import fibonacci
from .icosahedral import icosahedral
from .jacobsthal import jacobsthal
from .kynea import kynea
from .lazy_caterer import lazy_caterer
from .leonardo import leonardo
from .loeschian import loeschian
from .lucas import lucas
from .oblong import oblong
from .padovan import padovan
from .pell import pell
from .perfect import perfect
from .period2 import period2
from .perrin import perrin
from .polite import polite
from .polygonal import (
    decagonal,
    dodecagonal,
    hendecagonal,
    heptagonal,
    hexagonal,
    natural,
    nonagonal,
    octagonal,
    pentagonal,
    polygonal,
    square,
    triangular,
)
from .pyramidal import (
    heptagonal_pyramidal,
    hexagonal_pyramidal,
    octagonal_pyramidal,
    pentagonal_pyramidal,
    square_pyramidal,
    triangular_pyramidal,
)
from .quasiperfect import quasiperfect
from .recaman import recaman
from .semiperfect import semiperfect
from .superperfect import superperfect
from .sylvester import sylvester
from .totient import totient
from .tribonacci import tribonacci
from .vauban import vauban
from .weird import weird
from .woodall import woodall

__version__ = "0.1.7"
__all__ = [
    "abundant",
    "arithmetic",
    "buttered_croissant",
    "catalan",
    "centered_decagonal",
    "centered_dodecagonal",
    "centered_hendecagonal",
    "centered_heptagonal",
    "centered_hexagonal",
    "centered_nonagonal",
    "centered_octagonal",
    "centered_pentagonal",
    "centered_polygonal",
    "centered_square",
    "centered_triangular",
    "composite",
    "decagonal",
    "deficient",
    "dodecagonal",
    "eratosthenes",
    "factorial",
    "fibonacci",
    "hendecagonal",
    "heptagonal",
    "heptagonal_pyramidal",
    "hexagonal",
    "hexagonal_pyramidal",
    "icosahedral",
    "jacobsthal",
    "kynea",
    "lazy_caterer",
    "leonardo",
    "loeschian",
    "lucas",
    "natural",
    "nonagonal",
    "oblong",
    "octagonal",
    "octagonal_pyramidal",
    "padovan",
    "pell",
    "pentagonal",
    "pentagonal_pyramidal",
    "perfect",
    "period2",
    "perrin",
    "polite",
    "polygonal",
    "quasiperfect",
    "recaman",
    "semiperfect",
    "square",
    "sylvester",
    "square_pyramidal",
    "superperfect",
    "totient",
    "triangular",
    "triangular_pyramidal",
    "tribonacci",
    "vauban",
    "weird",
    "woodall",
]
