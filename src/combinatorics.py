from math import factorial


def permutations(n: int, k: int) -> int:
    """Number of ordered ways to choose k items from n."""
    if k < 0 or k > n:
        return 0
    return factorial(n) // factorial(n - k)


def combinations(n: int, k: int) -> int:
    """Number of unordered ways to choose k items from n (n choose k)."""
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))