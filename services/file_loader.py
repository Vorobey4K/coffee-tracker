import csv

def load_data(files):
    data = []

    for file in files:
        try:
            with open(file, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data.extend(reader)
        except FileNotFoundError:
            raise ValueError(f"File not found: {file}") from None

    return data