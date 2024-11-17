import employee_info as ei

def test_get_employees_by_age_range():
    expected_result = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
        ]
    result = ei.get_employees_by_age_range(20,30)
    assert (result == expected_result)

def test_calculate_average_salary():
    expected_result = 60166.66667
    result = ei.calculate_average_salary()
    assert (result == expected_result)

def test_get_employees_by_dept():
    expected_result = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    result = ei.get_employees_by_dept("Marketing")
    assert (result == expected_result)