import pytest

from calculator_utils import calculate_compound_interest


@pytest.mark.parametrize(
    ("frequency", "expected"),
    [
        ("monthly", 1126.8250301319697),
        ("quarterly", 1125.50881),
        ("annual", 1120.0),
    ],
)
def test_calculate_compound_interest_for_each_frequency(frequency, expected):
    assert calculate_compound_interest(1000, 0.12, 1, frequency) == pytest.approx(
        expected
    )


def test_calculate_compound_interest_handles_zero_and_large_values():
    assert calculate_compound_interest(0, 0.05, 10, "monthly") == 0
    assert calculate_compound_interest(1_000_000, 0, 2, "annual") == 1_000_000


@pytest.mark.parametrize(
    ("principal", "rate", "time_period", "frequency"),
    [
        (-1, 0.05, 1, "monthly"),
        (100, 0.05, -1, "quarterly"),
        (100, -12, 1, "monthly"),
        (100, 0.05, 1, "daily"),
        (100, 0.05, 1, []),
        (100, float("nan"), 1, "annual"),
        (100, 0.05, 1, "yearly"),
    ],
)
def test_calculate_compound_interest_rejects_invalid_inputs(
    principal, rate, time_period, frequency
):
    with pytest.raises(ValueError):
        calculate_compound_interest(principal, rate, time_period, frequency)


def test_calculate_compound_interest_rejects_overflow():
    with pytest.raises(ValueError, match="too large"):
        calculate_compound_interest(1e308, 1, 1, "annual")
