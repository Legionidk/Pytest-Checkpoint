import pytest
from schedule import get_subjects


@pytest.mark.parametrize(
    "day, result",
    [
        ("понедельник", ["Математика", "Программирование", "История"]),
        ("вторник", ["Физика"]),
        ("среда", ["Базы данных"]),
        ("четверг", ["Английский язык"]),
        ("пятница", ["Программирование", "Математика"]),
        ("суббота", ["Проектная деятельность"]),
        ("воскресенье", ["День открытых дверей", "Математика"]),
    ],
)
def test_get_subjects(shared_schedule, day, result):
    assert get_subjects(schedule=shared_schedule, day=day) == result
