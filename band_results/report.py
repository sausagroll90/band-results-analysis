from db import get_winners, get_wins_by_region
import csv

def format_row_for_printing(row):
    formatted_row = ""
    for key in row.keys():
        formatted_row += f"{key}: {row[key]}\n"
    return formatted_row

def print_winners(rows):
    #TODO use format_row_for_printing(), can for loop be abstracted out?
    for row in rows:
        print(f"band: {row['name']}")
        print(f"conductor: {row['conductor']}")
        print(f"year: {row['year']}")
        print(f"draw: {row['draw']}")
        print("")
    
    print(rows[0].keys())


def save_winners_to_txt_file(rows):
    with open("winners.txt", "w", encoding="utf-8") as f:
        for row in rows:
            formatted_row = f"band: {row['name']}, conductor: {row['conductor']}, year: {row['year']}, draw: {row['draw']}\n"
            f.write(formatted_row)


def save_winners_to_csv_file(rows):
    with open("winners.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            formatted_row = [row['name'], row['conductor'], row['year'], row['draw']]
            writer.writerow(formatted_row)


def print_wins_by_region(rows):
    for row in rows:
        print(f"region: {row['region']}")
        print(f"wins: {row['count(*)']}")
        print("")


def main():
    rows = get_winners()
    first_row = rows[0]
    print(format_row_for_printing(first_row))


if __name__ == "__main__":
    main()
