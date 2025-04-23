def second_variant_two_sum_1(dominoes: list[tuple[int, int]], target: int) -> int:
    """
    Counts the number of domino pairs that add up to a target value.

    Args:
        dominoes: A list of dominoes, where each domino is a pair of integers.
        target: The target sum for the domino pairs.

    Returns:
        The number of domino pairs whose elements sum up to the target.
    """
    domino_to_freq = defaultdict(lambda: 0)
    res = 0
    for a1, a2 in dominoes:
        b1 = target - a1
        b2 = target - a2

        if (b1, b2) in domino_to_freq:
            res += domino_to_freq[(b1, b2)]
        domino_to_freq[(a1, a2)] += 1 
    return res

def test_second_variant_two_sum_1():
    dominoes = [
        (3, 4),
        (1, 9),
        (3, 4),
        (2, 1),
        (9, 1),
        (9, 1),
        (7, 6),
        (1, 9)
    ]
    target = 10
    assert 6 == second_variant_two_sum_1(dominoes, target)

    dominoes = [  # Only digits 0-9 are permitted but these are just examples
        (1, 8),
        (12, 5),
        (12, 5),
        (12, 5),
    ]
    target = 13
    assert 3 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (1, 8),
        (12, 5),
        (12, 5),
        (12, 5),
        (1, 8)
    ]
    target = 13
    assert 6 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (1, 8),
        (12, 5),
        (12, 5),
        (12, 5),
        (1, 8),
        (12, 5),
    ]
    target = 13
    assert 8 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (1, 8),
        (1, 1),
        (5, 4),
        (1, 3),
        (1, 8),
        (12, 5),
    ]
    target = 300
    assert 0 == second_variant_two_sum_1(dominoes, target)

    dominoes = []
    target = 0
    assert 0 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (1, 2),
        (3, 2),
        (1, 2),
        (3, 2),
    ]
    target = 4
    assert 4 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0)
    ]
    target = 0
    assert 10 == second_variant_two_sum_1(dominoes, target)

    dominoes = [(3, 7)]
    target = 10
    assert 0 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (1, 9),
        (9, 1),
        (1, 9),
        (9, 1)
    ]
    target = 10
    assert 4 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    target = 10
    assert 0 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (1, 2),
        (3, 4),
        (0, 4)
    ]
    target = 1
    assert 0 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (9, 2),
        (4, 5),
        (3, 9),
        (9, 9),
        (2, 1),
        (2, 1),
        (2, 1)
    ]
    target = 6
    assert 3 == second_variant_two_sum_1(dominoes, target)

    dominoes = [
        (0, 9),
        (9, 0),
        (9, 0),
        (0, 9),
        (2, 1),
        (0, 9),
        (0, 9)
    ]
    target = 9
    assert 8 == second_variant_two_sum_1(dominoes, target)

# You can call the test function to verify the implementation
test_second_variant_two_sum_1()
