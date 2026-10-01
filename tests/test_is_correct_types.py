import pytest
from schedule import is_correct_types


@pytest.mark.parametrize(
    "day, result",
    [
        ("понедельник", True),
        ("вторник", True),
        ("среда", True),
        ("четверг", True),
        ("пятница", False),
        ("суббота", False),
        ("воскресенье", False),
    ],
)
def test_is_correct_types(shared_schedule, day, result):
    if day in ["суббота", "пятница"]:
        pytest.skip(f"Для дня не укзана спецификация: {day}")

    assert is_correct_types(schedule=shared_schedule, day=day) == result
