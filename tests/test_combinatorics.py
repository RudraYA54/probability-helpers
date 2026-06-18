from src.combinatorics import permutations, combinations


def test_combinations_basic():
    assert combinations(5, 2) == 10
    assert combinations(5, 0) == 1
    assert combinations(5, 5) == 1


def test_permutations_basic():
    assert permutations(5, 2) == 20
    assert permutations(5, 0) == 1


def test_edge_cases():
    assert combinations(3, 5) == 0
    assert permutations(3, 5) == 0