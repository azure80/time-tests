from times import time_range, compute_overlap_time
from pytest import raises

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    assert compute_overlap_time(large, short) == [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

def test_more_intervals_in_large():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    assert compute_overlap_time(large, short) == [('2010-01-12 10:30:00', '2010-01-12 10:45:00')]

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
    assert compute_overlap_time(large, short) == []

def test_negative_time_range():
    with raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
        

def test_edges():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00")
    assert compute_overlap_time(large, short) == []

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 08:00:00", "2010-01-12 10:00:00")
    assert compute_overlap_time(large, short) == []
