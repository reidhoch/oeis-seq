# coding=utf-8
# flake8: noqa
from itertools import islice
from typing import List

from oeis import (
    abundant,
    buttered_croissant,
    catalan,
    centered_decagonal,
    centered_dodecagonal,
    centered_hendecagonal,
    centered_heptagonal,
    centered_hexagonal,
    centered_nonagonal,
    centered_octagonal,
    centered_pentagonal,
    centered_square,
    centered_triangular,
    composite,
    decagonal,
    deficient,
    dodecagonal,
    eratosthenes,
    factorial,
    fibonacci,
    hendecagonal,
    heptagonal,
    heptagonal_pyramidal,
    hexagonal,
    hexagonal_pyramidal,
    jacobsthal,
    lazy_caterer,
    leonardo,
    loeschian,
    lucas,
    natural,
    nonagonal,
    oblong,
    octagonal,
    octagonal_pyramidal,
    padovan,
    pell,
    pentagonal,
    pentagonal_pyramidal,
    perfect,
    perrin,
    polite,
    recaman,
    semiperfect,
    square,
    square_pyramidal,
    superperfect,
    sylvester,
    totient,
    triangular,
    triangular_pyramidal,
    tribonacci,
    vauban,
    weird,
    woodall,
)
from oeis.superperfect import superperfect


def test_abundant() -> None:
    expected: List[int] = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54]
    actual: List[int] = list(islice(abundant(), 10))
    assert actual == expected


def test_buttered_croissant() -> None:
    expected: List[int] = [1, 3, 7, 19, 55, 163, 487, 1459, 4375, 13123]
    actual: List[int] = list(islice(buttered_croissant(), 10))
    assert actual == expected


def test_catalan() -> None:
    expected: List[int] = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
    actual: List[int] = list(islice(catalan(), 10))
    assert actual == expected


def test_centered_decagonal() -> None:
    expected: List[int] = [1, 11, 31, 61, 101, 151, 211, 281, 361, 451]
    actual: List[int] = list(islice(centered_decagonal(), 10))
    assert actual == expected


def test_centered_dodecagonal() -> None:
    expected: List[int] = [1, 13, 37, 73, 121, 181, 253, 337, 433, 541]
    actual: List[int] = list(islice(centered_dodecagonal(), 10))
    assert actual == expected


def test_centered_hendecagonal() -> None:
    expected: List[int] = [1, 12, 34, 67, 111, 166, 232, 309, 397, 496]
    actual: List[int] = list(islice(centered_hendecagonal(), 10))
    assert actual == expected


def test_centered_heptagonal() -> None:
    expected: List[int] = [1, 8, 22, 43, 71, 106, 148, 197, 253, 316]
    actual: List[int] = list(islice(centered_heptagonal(), 10))
    assert actual == expected


def test_centered_hexagonal() -> None:
    expected: List[int] = [1, 7, 19, 37, 61, 91, 127, 169, 217, 271]
    actual: List[int] = list(islice(centered_hexagonal(), 10))
    assert actual == expected


def test_centered_nonagonal() -> None:
    expected: List[int] = [1, 10, 28, 55, 91, 136, 190, 253, 325, 406]
    actual: List[int] = list(islice(centered_nonagonal(), 10))
    assert actual == expected


def test_centered_octagonal() -> None:
    expected: List[int] = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
    actual: List[int] = list(islice(centered_octagonal(), 10))
    assert actual == expected


def test_centered_pentagonal() -> None:
    expected: List[int] = [1, 6, 16, 31, 51, 76, 106, 141, 181, 226]
    actual: List[int] = list(islice(centered_pentagonal(), 10))
    assert actual == expected


def test_centered_triangular() -> None:
    expected: List[int] = [1, 4, 10, 19, 31, 46, 64, 85, 109, 136]
    actual: List[int] = list(islice(centered_triangular(), 10))
    assert actual == expected


def test_centered_square() -> None:
    expected: List[int] = [1, 5, 13, 25, 41, 61, 85, 113, 145, 181]
    actual: List[int] = list(islice(centered_square(), 10))
    assert actual == expected


def test_composite() -> None:
    expected: List[int] = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
    actual: List[int] = list(islice(composite(), 10))
    assert actual == expected


def test_decagonal() -> None:
    expected: List[int] = [0, 1, 10, 27, 52, 85, 126, 175, 232, 297]
    actual: List[int] = list(islice(decagonal(), 10))
    assert actual == expected


def test_dodecagonal() -> None:
    expected: List[int] = [0, 1, 12, 33, 64, 105, 156, 217, 288, 369]
    actual: List[int] = list(islice(dodecagonal(), 10))
    assert actual == expected


def test_deficient() -> None:
    expected: List[int] = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    actual: List[int] = list(islice(deficient(), 10))
    assert actual == expected


def test_eratosthenes() -> None:
    expected: List[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    actual: List[int] = list(islice(eratosthenes(), 10))
    assert actual == expected


def test_factorial() -> None:
    expected: List[int] = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    actual: List[int] = list(islice(factorial(), 10))
    assert actual == expected


def test_fibonacci() -> None:
    expected: List[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    actual: List[int] = list(islice(fibonacci(), 10))
    assert actual == expected


def test_pentagonal() -> None:
    expected: List[int] = [0, 1, 5, 12, 22, 35, 51, 70, 92, 117]
    actual: List[int] = list(islice(pentagonal(), 10))
    assert actual == expected


def test_hendecagonal() -> None:
    expected: List[int] = [0, 1, 11, 30, 58, 95, 141, 196, 260, 333]
    actual: List[int] = list(islice(hendecagonal(), 10))
    assert actual == expected


def test_heptagonal() -> None:
    expected: List[int] = [0, 1, 7, 18, 34, 55, 81, 112, 148, 189]
    actual: List[int] = list(islice(heptagonal(), 10))
    assert actual == expected


def test_heptagonal_pyramidal() -> None:
    expected: List[int] = [0, 1, 8, 26, 60, 115, 196, 308, 456, 645]
    actual: List[int] = list(islice(heptagonal_pyramidal(), 10))
    assert actual == expected


def test_hexagonal() -> None:
    expected: List[int] = [0, 1, 6, 15, 28, 45, 66, 91, 120, 153]
    actual: List[int] = list(islice(hexagonal(), 10))
    assert actual == expected


def test_hexagonal_pyramidal() -> None:
    expected: List[int] = [0, 1, 7, 22, 50, 95, 161, 252, 372, 525]
    actual: List[int] = list(islice(hexagonal_pyramidal(), 10))
    assert actual == expected


def test_jacobsthal() -> None:
    expected: List[int] = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171]
    actual: List[int] = list(islice(jacobsthal(), 10))
    assert actual == expected


def test_lazy_caterer() -> None:
    expected: List[int] = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]
    actual: List[int] = list(islice(lazy_caterer(), 10))
    assert actual == expected


def test_leonardo() -> None:
    expected: List[int] = [1, 1, 3, 5, 9, 15, 25, 41, 67, 109]
    actual: List[int] = list(islice(leonardo(), 10))
    assert actual == expected


def test_loeschian() -> None:
    expected: List[int] = [0, 1, 3, 4, 7, 9, 12, 13, 16, 19]
    actual: List[int] = list(islice(loeschian(), 10))
    assert actual == expected


def test_lucas() -> None:
    expected: List[int] = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
    actual: List[int] = list(islice(lucas(), 10))
    assert actual == expected


def test_natural() -> None:
    expected: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    actual: List[int] = list(islice(natural(), 10))
    assert actual == expected


def test_nonagonal() -> None:
    expected: List[int] = [0, 1, 9, 24, 46, 75, 111, 154, 204, 261]
    actual: List[int] = list(islice(nonagonal(), 10))
    assert actual == expected


def test_oblong() -> None:
    expected: List[int] = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
    actual: List[int] = list(islice(oblong(), 10))
    assert actual == expected


def test_octagonal() -> None:
    expected: List[int] = [0, 1, 8, 21, 40, 65, 96, 133, 176, 225]
    actual: List[int] = list(islice(octagonal(), 10))
    assert actual == expected


def test_octagonal_pyramidal() -> None:
    expected: List[int] = [0, 1, 9, 30, 70, 135, 231, 364, 540, 765]
    actual: List[int] = list(islice(octagonal_pyramidal(), 10))
    assert actual == expected


def test_padovan() -> None:
    expected: List[int] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    actual: List[int] = list(islice(padovan(), 10))
    assert actual == expected


def test_pell() -> None:
    expected: List[int] = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985]
    actual: List[int] = list(islice(pell(), 10))
    assert actual == expected


def test_pentagonal_pyramidal() -> None:
    expected: List[int] = [0, 1, 6, 18, 40, 75, 126, 196, 288, 405]
    actual: List[int] = list(islice(pentagonal_pyramidal(), 10))
    assert actual == expected


def test_perfect() -> None:
    expected: List[int] = [6, 28, 496, 8128]
    actual: List[int] = list(islice(perfect(), 4))
    assert actual == expected


def test_perrin() -> None:
    expected: List[int] = [3, 0, 2, 3, 2, 5, 5, 7, 10, 12]
    actual: List[int] = list(islice(perrin(), 10))
    assert actual == expected


def test_polite() -> None:
    expected: List[int] = [3, 5, 6, 7, 9, 10, 11, 12, 13, 14]
    actual: List[int] = list(islice(polite(), 10))
    assert actual == expected


def test_recaman() -> None:
    expected: List[int] = [0, 1, 3, 6, 2, 7, 13, 20, 12, 21]
    actual: List[int] = list(islice(recaman(), 10))
    assert actual == expected


def test_semiperfect() -> None:
    expected: List[int] = [6, 12, 18, 20, 24, 28, 30, 36, 40, 42]
    actual: List[int] = list(islice(semiperfect(), 10))
    assert actual == expected


def test_superperfect() -> None:
    expected: List[int] = [2, 4, 16, 64, 4096, 65536, 262144]
    actual: List[int] = list(islice(superperfect(), 7))
    assert actual == expected


def test_sylvester() -> None:
    expected: List[int] = [
        2,
        3,
        7,
        43,
        1807,
        3263443,
        10650056950807,
        113423713055421844361000443,
        12864938683278671740537145998360961546653259485195807,
    ]
    actual: List[int] = list(islice(sylvester(), 9))
    assert actual == expected


def test_totient() -> None:
    expected: List[int] = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
    actual: List[int] = list(islice(totient(), 10))
    assert actual == expected


def test_triangular() -> None:
    expected: List[int] = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    actual: List[int] = list(islice(triangular(), 10))
    assert actual == expected


def test_square() -> None:
    expected: List[int] = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    actual: List[int] = list(islice(square(), 10))
    assert actual == expected


def test_square_pyramidal() -> None:
    expected: List[int] = [0, 1, 5, 14, 30, 55, 91, 140, 204, 285]
    actual: List[int] = list(islice(square_pyramidal(), 10))
    assert actual == expected


def test_triangular_pyramidal() -> None:
    expected: List[int] = [0, 1, 4, 10, 20, 35, 56, 84, 120, 165]
    actual: List[int] = list(islice(triangular_pyramidal(), 10))
    assert actual == expected


def test_tribonacci() -> None:
    expected: List[int] = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    actual: List[int] = list(islice(tribonacci(), 10))
    assert actual == expected


def test_vauban() -> None:
    expected: List[int] = [0, 1, 3, 15, 69, 321, 1491, 6921, 32139, 149229]
    actual: List[int] = list(islice(vauban(), 10))
    assert actual == expected


def test_weird() -> None:
    expected: List[int] = [70, 836, 4030, 5830, 7192, 7912, 9272]
    actual: List[int] = list(islice(weird(), 7))
    assert actual == expected


def test_woodall() -> None:
    expected: List[int] = [1, 7, 23, 63, 159, 383, 895, 2047, 4607, 10239]
    actual: List[int] = list(islice(woodall(), 10))
    assert actual == expected
