import argparse
import csv
import openpyxl
import re

_WORKSHEET_TITLE_TO_CATEGORY_NAMES = {
    "LiqueursCordials": "Liqueurs and Cordials",
    "BrandyCognac": "Brandy and Cognac",
}

_WORKSHEETS_TO_SKIP = ["Order History"]

_CSV_COLUMN_TITLES = ["Category", "Name", "Price"]

_STRING_REPLACEMENTS = {
    '"': "",
    " (yr|year)": "yr",
    "proof": " proof",
    "WP ": "WhistlePig ",
}


_STRINGS_TO_LEAVE_UNFORMATTED = ["WhistlePig"]

_STRINGS_TO_UPPERCASE = ["IPA", "LALO", "OFTD", "VS", "VSOP", "XO"]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_filename", required=True)
    parser.add_argument("--output_filename", required=True)
    return parser.parse_args()


def is_roman_numeral(s):
    return re.match("^[MDCLXVI]+$", s, re.IGNORECASE)


def should_be_lowercase(s):
    return any(c.isdigit() for c in s)


def should_be_uppercase(s):
    return is_roman_numeral(s) or s.upper() in _STRINGS_TO_UPPERCASE


def format_value(value):
    for k, v in _STRING_REPLACEMENTS.items():
        value = re.sub(k, v, value, flags=re.IGNORECASE)

    formatted_parts = []
    for part in value.split():
        if part in _STRINGS_TO_LEAVE_UNFORMATTED:
            formatted_parts.append(part)
        elif should_be_lowercase(part):
            formatted_parts.append(part.lower())
        elif should_be_uppercase(part):
            formatted_parts.append(part.upper())
        else:
            formatted_parts.append(part.title())

    return " ".join(formatted_parts)


def parse_worksheet(worksheet):
    category = (
        _WORKSHEET_TITLE_TO_CATEGORY_NAMES[worksheet.title]
        if worksheet.title in _WORKSHEET_TITLE_TO_CATEGORY_NAMES
        else worksheet.title
    )

    values = []
    for row in worksheet:
        value = row[0].value
        if (
            not value
            or not value.strip()
            or value.strip().lower() == "name"
            or value.strip().lower().startswith("well ")
        ):
            continue

        price = int(row[2].value) if isinstance(row[2].value, float) else ""
        values.append([category, format_value(value), price])

    return values


def write_values_to_csv(filename, values):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(_CSV_COLUMN_TITLES)
        for row in values:
            writer.writerow(row)


def main():
    args = parse_args()
    wb = openpyxl.load_workbook(args.input_filename)
    values = []
    for i in wb.sheetnames:
        if i in _WORKSHEETS_TO_SKIP:
            continue

        values += parse_worksheet(wb[i])

    write_values_to_csv(args.output_filename, sorted(values))


if __name__ == "__main__":
    main()
