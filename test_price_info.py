import price_info as pi

def test_total_cost_shopping():
    expected_result = 46.75
    result = pi.total_cost_shopping()
    assert (result == expected_result)

def test_cost_of_fruit():
    expected_result = 4.5
    result = pi.cost_of_fruits('pear', 5)
    assert (result == expected_result)