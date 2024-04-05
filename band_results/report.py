from db import get_winners, get_wins_by_region
import csv


def print_rows_to_console(rows):
    for row in rows:
        formatted_row = format_row_for_console(row)
        print(formatted_row)


def format_row_for_console(row):
    formatted_row = ""
    for key in row.keys():
        formatted_row += format_key_value_for_console(key, row[key])
    return formatted_row


def format_key_value_for_console(key, value):
    if key == "count(*)":
        formatted_key_value = f"count: {value}\n"
    else:
        formatted_key_value = f"{key}: {value}\n"
    return formatted_key_value


def save_rows_to_file(file_path, rows):
    if file_path.endswith(".txt"):
        save_rows_to_txt(file_path, rows)
    elif file_path.endswith(".csv"):
        save_rows_to_csv(file_path, rows)
    else:
        raise ValueError("File extension must be .txt or .csv")


def save_rows_to_txt(file_path, rows):
    with open(file_path, "w", encoding="utf-8") as f:
        for row in rows:
            formatted_row = format_row_for_txt(row)
            f.write(formatted_row)


def format_row_for_txt(row):
    formatted_row = ""
    for key in row.keys():
        formatted_row += format_key_value_for_txt(key, row[key])
    trimmed_formatted_row = formatted_row[0:-2] + "\n"
    return trimmed_formatted_row


def format_key_value_for_txt(key, value):
    if key == "count(*)":
        formatted_row = f"count: {value}, "
    else:
        formatted_row = f"{key}: {value}, "
    return formatted_row


def save_rows_to_csv(file_path, rows):
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        header = make_csv_header(rows)
        writer.writerow(header)
        for row in rows:
            formatted_row = format_row_for_csv(row)
            writer.writerow(formatted_row)


def make_csv_header(rows):
    header = rows[0].keys()
    if "count(*)" in header:
        header[header.index("count(*)")] = "count"
    return header


def format_row_for_csv(row):
    formatted_row = [row[key] for key in row.keys()]
    return formatted_row


def main():
    winners = get_winners()
    wins_by_region = get_wins_by_region()
    save_rows_to_file("winners.txt", winners)
    save_rows_to_file("wins_by_region.txt", wins_by_region)
    save_rows_to_file("winners.csv", winners)
    save_rows_to_file("wins_by_region.csv", wins_by_region)


if __name__ == "__main__":
    main()
