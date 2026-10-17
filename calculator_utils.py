import math


def calculate_compound_interest(
    principal: float,
    rate: float,
    time_period: float,
    compounding_frequency: str,
) -> float:
    """Return the final balance using an annual decimal rate and time in years."""
    if not isinstance(compounding_frequency, str):
        raise ValueError(
            "compounding_frequency must be 'monthly', 'quarterly', or 'annual'"
        )
    periods_per_year = {"monthly": 12, "quarterly": 4, "annual": 1}.get(
        compounding_frequency
    )
    if periods_per_year is None:
        raise ValueError(
            "compounding_frequency must be 'monthly', 'quarterly', or 'annual'"
        )

    for value in (principal, rate, time_period):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("principal, rate, and time_period must be finite numbers")
        try:
            is_finite = math.isfinite(value)
        except OverflowError:
            is_finite = False
        if not is_finite:
            raise ValueError("principal, rate, and time_period must be finite numbers")

    if principal < 0 or time_period < 0 or rate <= -periods_per_year:
        raise ValueError(
            "principal and time_period must be non-negative and rate must exceed "
            f"{-periods_per_year}"
        )

    try:
        balance = principal * (1 + rate / periods_per_year) ** (
            periods_per_year * time_period
        )
    except OverflowError as error:
        raise ValueError("calculated balance is too large") from error
    if not math.isfinite(balance):
        raise ValueError("calculated balance is too large")
    return balance
