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


def save_rows_to_txt(rows):
    with open("winners.txt", "w", encoding="utf-8") as f:
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


def save_rows_to_csv(rows):
    with open("winners.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        header = rows[0].keys()
        writer.writerow(header)
        for row in rows:
            formatted_row = format_row_for_csv(row)
            writer.writerow(formatted_row)


def format_row_for_csv(row):
    formatted_row = [row[key] for key in row.keys()]
    return formatted_row


def main():
    winners = get_winners()
    save_rows_to_csv(winners)


if __name__ == "__main__":
    main()
