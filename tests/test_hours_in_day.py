import pytest
from schedule import hours_in_day


@pytest.mark.parametrize(
    "day, expected",
    [
        ("понедельник", 3.5),
        ("вторник", 2),
        ("среда", 2),
        ("четверг", 0),
        ("пятница", 0),
        ("суббота", 0),
        ("воскресенье", 1),
    ],
)
def test_hours_in_day(shared_schedule, day, expected):
    assert hours_in_day(schedule=shared_schedule, day=day) == expected
