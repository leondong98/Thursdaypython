import pytest

def range_overlap(ranges):
    """Return common overlap among a set of [left, right] ranges."""
    assert len(ranges) > 1, "You need more than one rangety"
    max_left, min_right = ranges[0]
    if type(max_left) is str:
        raise ValueError("The input should be numbers")
    for (left, right) in ranges:
        max_left = max(max_left, left)
        min_right = min(min_right, right)
    return (max_left, min_right)

def test_range_overlap():
    assert range_overlap([(0.0, 1.0)]) == (0.0, 1.0)
    assert range_overlap([(-3, 5), (0, 4.5), (-1.5, 2)]) == (0, 2)
    assert range_overlaprange_overlap([(-10, 10), (-0.1, 2.1), (-100, 100), (-0.01, 2.01)]) == (0, 2)

def test_errors():
    with pytest.raises(AssertionError):
       range_overlap([(0, 0), (1, 0)])
       range_overlap([(-5, 5), (6, 7)])
