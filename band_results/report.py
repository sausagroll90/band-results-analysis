from band_results.db import get_winners, get_wins_by_region, get_avg_draw_by_position
import csv


def format_key_value(key, value):
    if key == "COUNT(*)":
        formatted_row = f"count: {value}"
    else:
        formatted_row = f"{key}: {value}"
    return formatted_row


def print_rows_to_console(rows):
    for row in rows:
        formatted_row = format_row_for_console(row)
        print(formatted_row)


def format_row_for_console(row):
    formatted_row = ""
    for key in row.keys():
        formatted_row += format_key_value(key, row[key])
        formatted_row += "\n"
    return formatted_row


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
        formatted_row += format_key_value(key, row[key])
        formatted_row += ", "
    trimmed_formatted_row = formatted_row[0:-2] + "\n"
    return trimmed_formatted_row


def save_rows_to_csv(file_path, rows):
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        header = list(rows[0].keys())
        if "COUNT(*)" in header:
            header[header.index("COUNT(*)")] = "count"
        writer.writerow(header)

        for row in rows:
            writer.writerow(row.values())
