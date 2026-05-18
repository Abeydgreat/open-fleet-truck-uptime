import pytest
from cpk_calculator import calculate_cpk

def test_standard_cpk_calculation():
    purchase_price = 500000.0 + 1800000.0
    calculated_cpk = calculate_cpk(purchase_price, 136500.0, 282475.0, 2160000.0, 3600000.0, 527500.0, 480000.0)
    assert calculated_cpk == pytest.approx(18.76, abs=1e-2)

def test_zero_distance_handling():
    with pytest.raises(ZeroDivisionError):
        calculate_cpk(2300000, 136500, 282475, 2160000, 3600000, 527500, 0)
