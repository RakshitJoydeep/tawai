import argparse
import csv
import random
from pathlib import Path
from typing import List, Dict

TEMPLATES = [
    "{Business} presents {Product}! {Description} Perfect for {Audience}. {Offer} {CTA}",
    "Discover {Product} from {Business}: {Description} Ideal for {Audience}. {Offer} {CTA}",
    "Need {Product}? {Business} has you covered. {Description} {Offer} {CTA}",
    "🚀 {Product} by {Business}! {Description} Great for {Audience}. {Offer} {CTA}",
]


def load_rows(path: Path) -> List[Dict[str, str]]:
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def generate_creative(data: Dict[str, str]) -> str:
    template = random.choice(TEMPLATES)
    return template.format(
        Business=data.get('business', '').strip(),
        Product=data.get('product', '').strip(),
        Description=data.get('description', '').strip(),
        Audience=data.get('audience', '').strip(),
        Offer=data.get('offer', '').strip(),
        CTA=data.get('cta', '').strip(),
    )


def generate_creatives(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    for row in rows:
        row['creative'] = generate_creative(row)
    return rows


def write_rows(rows: List[Dict[str, str]], path: Path):
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate meta ad creatives from CSV data')
    parser.add_argument('input', help='Path to input CSV file')
    parser.add_argument('output', help='Path to output CSV file')
    return parser.parse_args()


def main():
    args = parse_args()
    rows = load_rows(Path(args.input))
    rows = generate_creatives(rows)
    write_rows(rows, Path(args.output))
    print(f"Generated {len(rows)} ad creatives in {args.output}")


if __name__ == '__main__':
    main()
