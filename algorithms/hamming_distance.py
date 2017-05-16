def hamming_distance(vector1: iterable, vector2: iterable) -> int:
    # TODO
    pass

assert hamming_distance([],[]) == 0
assert hamming_distance([0,1],[0,1]) == 0
assert hamming_distance("00","01") == 1
assert hamming_distance("karolin", "kathrin") == 3
assert hamming_distance("karolin", "kerstin") == 3
assert hamming_distance((1,0,1,1,1,0,1), (1,0,0,1,0,0,1)) == 2
assert hamming_distance("2173896", "2233796") == 3
