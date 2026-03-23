import pytest
from main import main
import sys


@pytest.mark.parametrize(
    "argv, expect_exit, expect_err",
    [
        # валидный файл + валидный отчёт
        (["main.py", "--files", "valid.csv", "--report", "median-coffee"], False, None),
        # валидный файл + неизвестный отчёт
        (["main.py", "--files", "valid.csv", "--report", "unknown"], True, "unknown report"),
        # несуществующий файл + валидный отчёт
        (["main.py", "--files", "missing.csv", "--report", "median-coffee"], True, "file not found"),
        # несуществующий файл + неизвестный отчёт
        (["main.py", "--files", "missing.csv", "--report", "unknown"], True, "unknown report"),
    ]
)
def test_main_combinations(monkeypatch, capsys, tmp_path, argv, expect_exit, expect_err):

    valid_file = tmp_path / "valid.csv"
    valid_file.write_text("student,coffee_spent\nA,100\n")

    monkeypatch.setattr(
        sys,
        "argv",
        [a.replace("valid.csv", str(valid_file)) for a in argv]
    )

    if expect_exit:
        with pytest.raises(SystemExit):
            main()
        captured = capsys.readouterr()
        assert expect_err.lower() in captured.err.lower()
    else:
        main()
        captured = capsys.readouterr()
        assert "A" in captured.out