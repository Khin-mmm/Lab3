from Lab2_practice import bmi as bmi

def test_calculate_bmi_underweight():
    result = bmi.calculate_bmi(weight=35, height=1.5)
    assert(result == -1)

def test_calculate_bmi_normalweight():
    result = bmi.calculate_bmi(weight=50, height=1.5)
    assert(result == 0)

def test_calculate_bmi_overweight():
    result = bmi.calculate_bmi(weight=60, height=1.5)
    assert(result == 1)