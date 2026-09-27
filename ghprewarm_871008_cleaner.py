# language: Python 3, file: cleaner.py
import csv, sys, argparse


def clean_csv(path, out_path, dedupe=True):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    header, body = rows[0], rows[1:]
    body = [[c.strip() for c in r] for r in body]
    if dedupe:
        seen, uniq = set(), []
        for r in body:
            k = tuple(r)
            if k not in seen:
                seen.add(k); uniq.append(r)
        body = uniq
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(body)
    return len(body)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input"); p.add_argument("-o", "--output", default="cleaned.csv")
    p.add_argument("--no-dedupe", action="store_true")
    a = p.parse_args()
    n = clean_csv(a.input, a.output, dedupe=not a.no_dedupe)
    print(f"wrote {n} rows to {a.output}")


if __name__ == "__main__":
    main()
