from times import time_range, compute_overlap_time
from pytest import raises
import pytest

def test_negative_time_range():
    with raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")


@pytest.mark.parametrize("range1, range2, expected", [(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60), [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
                                            (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00"), [('2010-01-12 10:30:00', '2010-01-12 10:45:00')]),
                                            (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00"), []),
                                            (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00"), []),
                                            (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 08:00:00", "2010-01-12 10:00:00"), [])])
def test_various_time_overlaps(range1, range2, expected):
    assert compute_overlap_time(range1, range2) == expected