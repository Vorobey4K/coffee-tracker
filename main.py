
import argparse
import sys

from reports import REPORTS
from tabulate import tabulate
from services.file_loader import load_data


def parse_args():
    parser = argparse.ArgumentParser(description="Generate reports from CSV files")

    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
    )

    parser.add_argument(
        '--report',
        required=True,
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.report not in REPORTS:
        print(f"Error: unknown report '{args.report}'", file=sys.stderr)
        print(f"Available reports: {', '.join(REPORTS.keys())}", file=sys.stderr)
        sys.exit(1)

    try:
        data = load_data(args.files)
    except ValueError as e:
        print(f"Error loading files: {e}", file=sys.stderr)
        sys.exit(1)

    report_instance = REPORTS[args.report]()
    report_result = report_instance.generate(data)

    table = [(entity, metric) for entity, metric in report_result.items()]

    print(tabulate(
        table,
        headers=[report_instance.group_field.title(),
                 report_instance.value_field.title()],
        tablefmt="grid"
    ))


if __name__ == '__main__':
    main()