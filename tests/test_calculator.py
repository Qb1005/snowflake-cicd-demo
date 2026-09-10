from src.calculator import (
    calculate_revenue,
    calculate_discount
)


def test_calculate_revenue():
    result = calculate_revenue(10, 5)
    assert result == 50


def test_calculate_discount():
    result = calculate_discount(100, 0.10)
    assert result == 10