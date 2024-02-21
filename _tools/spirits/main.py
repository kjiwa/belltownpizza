import argparse
import csv
import openpyxl
import os.path
import re
import schema
import yaml

_CFG_SCHEMA = schema.Schema(
    {
        "exclude_worksheets": list,
        "output_column_names": list,
        "rename_worksheets": dict,
        "string_substitutions": dict,
        "strings_to_ignore": list,
        "strings_to_leave_unformatted": list,
        "strings_to_uppercase": list,
    }
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="spirits.yaml")
    parser.add_argument("--input_filename", default="spirits.xlsx")
    parser.add_argument("--output_filename", default="spirits.csv")
    return parser.parse_args()


def load_config(config_file):
    if not os.path.isfile(config_file):
        raise Exception('Configuration file "{}" does not exist.'.format(config_file))

    with open(config_file, "r") as f:
        cfg = yaml.safe_load(f)
        _CFG_SCHEMA.validate(cfg)
        return cfg


def is_roman_numeral(s):
    return re.match("^[MDCLXVI]+$", s, re.IGNORECASE)


def should_be_lowercase(s):
    return any(c.isdigit() for c in s)


def should_be_uppercase(s, cfg):
    return is_roman_numeral(s) or s.upper() in cfg["strings_to_uppercase"]


def format_value(value, cfg):
    for k, v in cfg["string_substitutions"].items():
        value = re.sub(k, v, value, flags=re.IGNORECASE)

    formatted_parts = []
    for part in value.split():
        if part in cfg["strings_to_leave_unformatted"]:
            formatted_parts.append(part)
        elif should_be_lowercase(part):
            formatted_parts.append(part.lower())
        elif should_be_uppercase(part, cfg):
            formatted_parts.append(part.upper())
        else:
            formatted_parts.append(part.title())

    return " ".join(formatted_parts)


def parse_worksheet(worksheet, cfg):
    category = (
        cfg["rename_worksheets"][worksheet.title]
        if worksheet.title in cfg["rename_worksheets"]
        else worksheet.title
    )

    values = []
    for row in worksheet:
        value = row[0].value
        if not value or not value.strip():
            continue

        skip_value = False
        for i in cfg["strings_to_ignore"]:
            if re.match(i, value.strip().lower(), re.IGNORECASE):
                skip_value = True
                break

        if skip_value:
            continue

        price = int(row[2].value) if isinstance(row[2].value, float) else ""
        values.append([category, format_value(value, cfg), price])

    return values


def write_values_to_csv(filename, values, cfg):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(cfg["output_column_names"])
        for row in values:
            writer.writerow(row)


def main():
    args = parse_args()
    cfg = load_config(args.config)

    wb = openpyxl.load_workbook(args.input_filename)
    values = []
    for i in wb.sheetnames:
        if i in cfg["exclude_worksheets"]:
            continue

        values += parse_worksheet(wb[i], cfg)

    write_values_to_csv(args.output_filename, sorted(values), cfg)


if __name__ == "__main__":
    main()
