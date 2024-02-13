import argparse
import csv
import openpyxl

_WORKSHEET_TITLE_TO_CATEGORY_NAMES = {
    "LiqueursCordials": "Liqueurs and Cordials",
    "BrandyCognac": "Brandy and Cognac",
}

_WORKSHEETS_TO_SKIP = ["Order History"]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_filename", required=True)
    parser.add_argument("--output_filename", required=True)
    return parser.parse_args()


def format_value(value):
    formatted_parts = []
    for part in value.split(" "):
        if part[0].isdigit():
            formatted_parts.append(part.lower())
        elif part.islower():
            formatted_parts.append(part.title())
        else:
            formatted_parts.append(part)

    return " ".join(formatted_parts).replace('"', "")


def parse_worksheet(worksheet):
    category = (
        _WORKSHEET_TITLE_TO_CATEGORY_NAMES[worksheet.title]
        if worksheet.title in _WORKSHEET_TITLE_TO_CATEGORY_NAMES
        else worksheet.title
    )

    values = []
    for row in worksheet:
        value = row[0].value
        if not value or not value.strip() or value.strip().lower() == "name":
            continue

        values.append([category, format_value(value)])

    return values


def write_values_to_csv(filename, values):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        for row in values:
            writer.writerow(row)


def main():
    args = parse_args()
    wb = openpyxl.load_workbook(args.input_filename)
    values = []
    for i in sorted(wb.sheetnames):
        if i in _WORKSHEETS_TO_SKIP:
            continue

        values += parse_worksheet(wb[i])

    write_values_to_csv(args.output_filename, values)


if __name__ == "__main__":
    main()
