from typing import Iterable
import unittest


def hamming_distance(vector1: Iterable, vector2: Iterable) -> int:
    distance = 0

    for e1, e2 in zip(vector1, vector2):
        if e1 != e2:
            distance += 1

    if len(vector2) > len(vector1):
        distance += len(vector2) - len(vector1)

    if len(vector1) > len(vector2):
        distance += len(vector1) - len(vector2)

    return distance


class TestHammingDistance(unittest.TestCase):
    def test_given(self):
        assert hamming_distance([], []) == 0
        assert hamming_distance([0, 1], [0, 1]) == 0
        assert hamming_distance("00", "01") == 1
        assert hamming_distance("karolin", "kathrin") == 3
        assert hamming_distance("karolin", "kerstin") == 3
        assert hamming_distance((1, 0, 1, 1, 1, 0, 1), (1, 0, 0, 1, 0, 0, 1)) == 2
        assert hamming_distance("2173896", "2233796") == 3

    def test_unequal_len(self):
        assert hamming_distance([0, 1], [0, 1, 2]) == 1
        assert hamming_distance([0, 1, 2], [0, 1]) == 1
        assert hamming_distance("kathy", "kathryn") == 3
        assert hamming_distance("kathryn", "kathy") == 3
        assert hamming_distance((), (1, 2, 3, 4)) == 4
        assert hamming_distance((1, 2, 3, 4), ()) == 4


if __name__ == '__main__':
    unittest.main()
