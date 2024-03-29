# flake8: noqa
from itertools import islice

from pytest import raises

from oeis import (
    abundant,
    arithmetic,
    buttered_croissant,
    carmichael,
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
    fermat,
    fibonacci,
    hendecagonal,
    heptagonal,
    heptagonal_pyramidal,
    hexagonal,
    hexagonal_pyramidal,
    hilbert,
    icosahedral,
    jacobsthal,
    juggler,
    kynea,
    lazy_caterer,
    leonardo,
    loeschian,
    lucas,
    mersenne,
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
    period2,
    perrin,
    polite,
    quasiperfect,
    recaman,
    rough,
    rough2,
    rough3,
    rough5,
    rough7,
    rough11,
    rough13,
    rough17,
    rough19,
    rough23,
    semiperfect,
    smooth,
    smooth2,
    smooth3,
    smooth5,
    smooth7,
    smooth11,
    smooth13,
    smooth17,
    smooth19,
    smooth23,
    sorting,
    square,
    square_pyramidal,
    squarefree,
    superperfect,
    sylvester,
    totient,
    triangular,
    triangular_pyramidal,
    tribonacci,
    unusual,
    vauban,
    weird,
    woodall,
)


def test_abundant() -> None:
    expected: list[int] = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54]
    actual: list[int] = list(islice(abundant(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_arithmetic() -> None:
    expected: list[int] = [1, 3, 5, 6, 7, 11, 13, 14, 15, 17]
    actual: list[int] = list(islice(arithmetic(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_buttered_croissant() -> None:
    expected: list[int] = [1, 3, 7, 19, 55, 163, 487, 1459, 4375, 13123]
    actual: list[int] = list(islice(buttered_croissant(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_carmichael() -> None:
    expected: list[int] = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341]
    actual: list[int] = list(islice(carmichael(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_catalan() -> None:
    expected: list[int] = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
    actual: list[int] = list(islice(catalan(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_decagonal() -> None:
    expected: list[int] = [1, 11, 31, 61, 101, 151, 211, 281, 361, 451]
    actual: list[int] = list(islice(centered_decagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_dodecagonal() -> None:
    expected: list[int] = [1, 13, 37, 73, 121, 181, 253, 337, 433, 541]
    actual: list[int] = list(islice(centered_dodecagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_hendecagonal() -> None:
    expected: list[int] = [1, 12, 34, 67, 111, 166, 232, 309, 397, 496]
    actual: list[int] = list(islice(centered_hendecagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_heptagonal() -> None:
    expected: list[int] = [1, 8, 22, 43, 71, 106, 148, 197, 253, 316]
    actual: list[int] = list(islice(centered_heptagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_hexagonal() -> None:
    expected: list[int] = [1, 7, 19, 37, 61, 91, 127, 169, 217, 271]
    actual: list[int] = list(islice(centered_hexagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_nonagonal() -> None:
    expected: list[int] = [1, 10, 28, 55, 91, 136, 190, 253, 325, 406]
    actual: list[int] = list(islice(centered_nonagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_octagonal() -> None:
    expected: list[int] = [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
    actual: list[int] = list(islice(centered_octagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_pentagonal() -> None:
    expected: list[int] = [1, 6, 16, 31, 51, 76, 106, 141, 181, 226]
    actual: list[int] = list(islice(centered_pentagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_triangular() -> None:
    expected: list[int] = [1, 4, 10, 19, 31, 46, 64, 85, 109, 136]
    actual: list[int] = list(islice(centered_triangular(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_centered_square() -> None:
    expected: list[int] = [1, 5, 13, 25, 41, 61, 85, 113, 145, 181]
    actual: list[int] = list(islice(centered_square(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_composite() -> None:
    expected: list[int] = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
    actual: list[int] = list(islice(composite(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_decagonal() -> None:
    expected: list[int] = [0, 1, 10, 27, 52, 85, 126, 175, 232, 297]
    actual: list[int] = list(islice(decagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_dodecagonal() -> None:
    expected: list[int] = [0, 1, 12, 33, 64, 105, 156, 217, 288, 369]
    actual: list[int] = list(islice(dodecagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_deficient() -> None:
    expected: list[int] = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    actual: list[int] = list(islice(deficient(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_eratosthenes() -> None:
    expected: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    actual: list[int] = list(islice(eratosthenes(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_factorial() -> None:
    expected: list[int] = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    actual: list[int] = list(islice(factorial(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_fermat() -> None:
    expected: list[int] = [3, 5, 17, 257, 65537, 4294967297, 18446744073709551617]
    actual: list[int] = list(islice(fermat(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_fibonacci() -> None:
    expected: list[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    actual: list[int] = list(islice(fibonacci(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_pentagonal() -> None:
    expected: list[int] = [0, 1, 5, 12, 22, 35, 51, 70, 92, 117]
    actual: list[int] = list(islice(pentagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_hendecagonal() -> None:
    expected: list[int] = [0, 1, 11, 30, 58, 95, 141, 196, 260, 333]
    actual: list[int] = list(islice(hendecagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_heptagonal() -> None:
    expected: list[int] = [0, 1, 7, 18, 34, 55, 81, 112, 148, 189]
    actual: list[int] = list(islice(heptagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_heptagonal_pyramidal() -> None:
    expected: list[int] = [0, 1, 8, 26, 60, 115, 196, 308, 456, 645]
    actual: list[int] = list(islice(heptagonal_pyramidal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_hexagonal() -> None:
    expected: list[int] = [0, 1, 6, 15, 28, 45, 66, 91, 120, 153]
    actual: list[int] = list(islice(hexagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_hexagonal_pyramidal() -> None:
    expected: list[int] = [0, 1, 7, 22, 50, 95, 161, 252, 372, 525]
    actual: list[int] = list(islice(hexagonal_pyramidal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_icosahedral() -> None:
    expected: list[int] = [1, 12, 48, 124, 255, 456, 742, 1128, 1629, 2260]
    actual: list[int] = list(islice(icosahedral(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_jacobsthal() -> None:
    expected: list[int] = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171]
    actual: list[int] = list(islice(jacobsthal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_juggler() -> None:
    expected: list[int] = [0, 1, 1, 5, 2, 11, 2, 18, 2, 27, 3, 36, 3, 46, 3, 58]
    actual: list[int] = list(islice(juggler(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_kynea() -> None:
    expected: list[int] = [7, 23, 79, 287, 1087, 4223, 16639, 66047, 263167, 1050623]
    actual: list[int] = list(islice(kynea(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_lazy_caterer() -> None:
    expected: list[int] = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]
    actual: list[int] = list(islice(lazy_caterer(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_leonardo() -> None:
    expected: list[int] = [1, 1, 3, 5, 9, 15, 25, 41, 67, 109]
    actual: list[int] = list(islice(leonardo(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_loeschian() -> None:
    expected: list[int] = [0, 1, 3, 4, 7, 9, 12, 13, 16, 19]
    actual: list[int] = list(islice(loeschian(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_lucas() -> None:
    expected: list[int] = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
    actual: list[int] = list(islice(lucas(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_mersenne() -> None:
    expected: list[int] = [
        3,
        7,
        31,
        127,
        2047,
        8191,
        131071,
        524287,
        8388607,
        536870911,
    ]
    actual: list[int] = list(islice(mersenne(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_natural() -> None:
    expected: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    actual: list[int] = list(islice(natural(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_nonagonal() -> None:
    expected: list[int] = [0, 1, 9, 24, 46, 75, 111, 154, 204, 261]
    actual: list[int] = list(islice(nonagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_oblong() -> None:
    expected: list[int] = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
    actual: list[int] = list(islice(oblong(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_octagonal() -> None:
    expected: list[int] = [0, 1, 8, 21, 40, 65, 96, 133, 176, 225]
    actual: list[int] = list(islice(octagonal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_octagonal_pyramidal() -> None:
    expected: list[int] = [0, 1, 9, 30, 70, 135, 231, 364, 540, 765]
    actual: list[int] = list(islice(octagonal_pyramidal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_padovan() -> None:
    expected: list[int] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    actual: list[int] = list(islice(padovan(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_pell() -> None:
    expected: list[int] = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985]
    actual: list[int] = list(islice(pell(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_pentagonal_pyramidal() -> None:
    expected: list[int] = [0, 1, 6, 18, 40, 75, 126, 196, 288, 405]
    actual: list[int] = list(islice(pentagonal_pyramidal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_perfect() -> None:
    expected: list[int] = [6, 28, 496, 8128]
    actual: list[int] = list(islice(perfect(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_period2() -> None:
    expected: list[int] = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    actual: list[int] = list(islice(period2(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_perrin() -> None:
    expected: list[int] = [3, 0, 2, 3, 2, 5, 5, 7, 10, 12]
    actual: list[int] = list(islice(perrin(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_polite() -> None:
    expected: list[int] = [3, 5, 6, 7, 9, 10, 11, 12, 13, 14]
    actual: list[int] = list(islice(polite(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_quasiperfect() -> None:
    expected: list[int] = [20, 104, 464, 650, 1952, 130304, 522752]
    actual: list[int] = list(islice(quasiperfect(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_recaman() -> None:
    expected: list[int] = [0, 1, 3, 6, 2, 7, 13, 20, 12, 21]
    actual: list[int] = list(islice(recaman(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_rough_bad_k() -> None:
    with raises(ValueError):
        list(islice(rough(1), 10))


def test_rough2() -> None:
    expected: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual: list[int] = list(islice(rough2(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_rough3() -> None:
    expected: list[int] = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    actual: list[int] = list(islice(rough3(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_rough5() -> None:
    expected: list[int] = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29]
    actual: list[int] = list(islice(rough5(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_rough7() -> None:
    expected: list[int] = [1, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    actual: list[int] = list(islice(rough7(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_rough11() -> None:
    expected: list[int] = [1, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    actual: list[int] = list(islice(rough11(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_rough13() -> None:
    expected: list[int] = [1, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    actual: list[int] = list(islice(rough13(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_rough17() -> None:
    expected: list[int] = [1, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    actual: list[int] = list(islice(rough17(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_rough19() -> None:
    expected: list[int] = [1, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    actual: list[int] = list(islice(rough19(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_rough23() -> None:
    expected: list[int] = [1, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    actual: list[int] = list(islice(rough23(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_semiperfect() -> None:
    expected: list[int] = [6, 12, 18, 20, 24, 28, 30, 36, 40, 42]
    actual: list[int] = list(islice(semiperfect(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_smooth_bad_n() -> None:
    with raises(ValueError):
        list(islice(smooth(1), 10))


def test_smooth2() -> None:
    expected: list[int] = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    actual: list[int] = list(islice(smooth2(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_smooth3() -> None:
    expected: list[int] = [1, 2, 3, 4, 6, 8, 9, 12, 16, 18]
    actual: list[int] = list(islice(smooth3(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_smooth5() -> None:
    expected: list[int] = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
    actual: list[int] = list(islice(smooth5(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_smooth7() -> None:
    expected: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual: list[int] = list(islice(smooth7(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_smooth11() -> None:
    expected: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual: list[int] = list(islice(smooth11(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_smooth13() -> None:
    expected: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual: list[int] = list(islice(smooth13(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_smooth17() -> None:
    expected: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual: list[int] = list(islice(smooth17(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_smooth19() -> None:
    expected: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual: list[int] = list(islice(smooth19(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_smooth23() -> None:
    expected: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual: list[int] = list(islice(smooth23(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_squarefree() -> None:
    expected: list[int] = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22]
    actual: list[int] = list(islice(squarefree(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_superperfect() -> None:
    expected: list[int] = [2, 4, 16, 64, 4096, 65536, 262144]
    actual: list[int] = list(islice(superperfect(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_sylvester() -> None:
    expected: list[int] = [
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
    actual: list[int] = list(islice(sylvester(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_totient() -> None:
    expected: list[int] = [1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
    actual: list[int] = list(islice(totient(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_triangular() -> None:
    expected: list[int] = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    actual: list[int] = list(islice(triangular(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_square() -> None:
    expected: list[int] = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    actual: list[int] = list(islice(square(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_square_pyramidal() -> None:
    expected: list[int] = [0, 1, 5, 14, 30, 55, 91, 140, 204, 285]
    actual: list[int] = list(islice(square_pyramidal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_triangular_pyramidal() -> None:
    expected: list[int] = [0, 1, 4, 10, 20, 35, 56, 84, 120, 165]
    actual: list[int] = list(islice(triangular_pyramidal(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_tribonacci() -> None:
    expected: list[int] = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    actual: list[int] = list(islice(tribonacci(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_unusual() -> None:
    expected: list[int] = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 20, 21, 22, 23]
    actual: list[int] = list(islice(unusual(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_vauban() -> None:
    expected: list[int] = [0, 1, 3, 15, 69, 321, 1491, 6921, 32139, 149229]
    actual: list[int] = list(islice(vauban(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_weird() -> None:
    expected: list[int] = [70, 836, 4030, 5830, 7192, 7912, 9272]
    actual: list[int] = list(islice(weird(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_woodall() -> None:
    expected: list[int] = [1, 7, 23, 63, 159, 383, 895, 2047, 4607, 10239]
    actual: list[int] = list(islice(woodall(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_hilbert() -> None:
    expected: list[int] = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41]
    actual: list[int] = list(islice(hilbert(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])


def test_sorting() -> None:
    expected: list[int] = [0, 1, 3, 5, 8, 11, 14, 17, 21, 25, 29, 33, 37]
    actual: list[int] = list(islice(sorting(), len(expected)))
    assert all([a == b for a, b in zip(actual, expected)])
