import pytest
from schedule import SCHEDULE


@pytest.fixture(scope="class")
def shared_schedule():
    return SCHEDULE
