import pytest

from reports.median_coffee import MedianCoffeeReport


def test_median_odd():
    data = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "200"},
        {"student": "A", "coffee_spent": "300"},
    ]
    report = MedianCoffeeReport()
    result = report.generate(data)
    assert result["A"] == 200

def test_median_even():
    data = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "200"},
    ]
    report = MedianCoffeeReport()
    result = report.generate(data)
    assert result["A"] == 150

def test_sorted_desc():
    data = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "200"},
        {"student": "B", "coffee_spent": "500"},
        {"student": "B", "coffee_spent": "600"},
    ]
    report = MedianCoffeeReport()
    result = report.generate(data)
    keys = list(result.keys())
    assert keys == ["B", "A"]