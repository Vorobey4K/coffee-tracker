import pytest
from services.file_loader import load_data


def test_load_data_success(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("student,coffee_spent\nA,100\n")
    data = load_data([str(file)])
    assert len(data) == 1
    assert data[0]["student"] == "A"

def test_file_not_found():
    with pytest.raises(ValueError):
        load_data(["not_exists.csv"])

def test_load_multiple_files(tmp_path):
    file1 = tmp_path / "f1.csv"
    file2 = tmp_path / "f2.csv"
    file1.write_text("student,coffee_spent\nA,100\n")
    file2.write_text("student,coffee_spent\nA,200\n")
    data = load_data([str(file1), str(file2)])
    assert len(data) == 2