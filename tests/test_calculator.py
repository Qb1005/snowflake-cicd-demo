from src.calculator import calculate_revenue

def test_calculate_revenue():
    result = calculate_revenue(10,5)
    assert result == 50