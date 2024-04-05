from db import get_winners, get_wins_by_region
import csv


def format_row_for_printing(row):
    formatted_row = ""
    for key in row.keys():
        if key == "count(*)":
            formatted_row += f"count: {row[key]}\n"
        else:
            formatted_row += f"{key}: {row[key]}\n"

    return formatted_row


def print_rows(rows):
    for row in rows:
        formatted_row = format_row_for_printing(row)
        print(formatted_row)


def format_row_for_txt(row):
    formatted_row = ""
    for key in row.keys():
        if key == "count(*)":
            formatted_row += f"count: {row[key]}, "
        else:
            formatted_row += f"{key}: {row[key]}, "
    formatted_row += "\n"
    #TODO make the end of each row not have a comma and a space
    return formatted_row


def save_rows_to_txt_file(rows):
    with open("winners.txt", "w", encoding="utf-8") as f:
        for row in rows:
            formatted_row = format_row_for_txt(row)
            f.write(formatted_row)


def save_winners_to_csv_file(rows):
    with open("winners.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            formatted_row = [row['name'], row['conductor'], row['year'], row['draw']]
            writer.writerow(formatted_row)


def main():
    rows = get_winners()
    save_rows_to_txt_file(rows)


if __name__ == "__main__":
    main()
