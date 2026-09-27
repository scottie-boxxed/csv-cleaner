# language: Python 3, file: cleaner.py
import csv
import sys
import argparse


def clean_csv(path, out_path, dedupe=True):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    header, body = rows[0], rows[1:]
    body = [[cell.strip() for cell in row] for row in body]
    if dedupe:
        seen, unique = set(), []
        for row in body:
            key = tuple(row)
            if key not in seen:
                seen.add(key)
                unique.append(row)
        body = unique
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(body)
    return len(body)


def main():
    parser = argparse.ArgumentParser(description="Clean a CSV file")
    parser.add_argument("input")
    parser.add_argument("-o", "--output", default="cleaned.csv")
    parser.add_argument("--no-dedupe", action="store_true")
    args = parser.parse_args()
    count = clean_csv(args.input, args.output, dedupe=not args.no_dedupe)
    print(f"wrote {count} rows to {args.output}")


if __name__ == "__main__":
    main()
