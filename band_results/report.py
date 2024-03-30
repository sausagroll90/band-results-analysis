from db import get_winners
import csv

def print_winners(rows):
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


def main():
    rows = get_winners()
    print_winners(rows)
    save_winners_to_txt_file(rows)
    save_winners_to_csv_file(rows)


if __name__ == "__main__":
    main()
