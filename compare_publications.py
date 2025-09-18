#!/usr/bin/env python3
import csv
import re
from bs4 import BeautifulSoup

def extract_csv_publications(csv_file):
    """Extract all publications from CSV file starting from row 5"""
    publications = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        # Skip first 4 rows (header information)
        for i in range(4):
            next(csv_reader)

        for row_num, row in enumerate(csv_reader, start=5):
            if len(row) >= 7 and row[1].strip():  # Check if title exists
                pub = {
                    'row_number': row_num,
                    'sr_no': row[0].strip(),
                    'title': row[1].strip(),
                    'author': row[2].strip(),
                    'journal': row[3].strip(),
                    'year': row[4].strip(),
                    'issn': row[5].strip(),
                    'classification': row[6].strip()
                }
                publications.append(pub)

    return publications

def extract_html_publications(html_file):
    """Extract all publications from HTML table"""
    publications = []

    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Find the table in collapseFour div
    collapse_div = soup.find('div', id='collapseFour')
    if not collapse_div:
        print("Could not find collapseFour div")
        return publications

    table = collapse_div.find('table')
    if not table:
        print("Could not find table in collapseFour")
        return publications

    # Extract rows from table body
    tbody = table.find('tbody')
    if tbody:
        rows = tbody.find_all('tr')
        print(f"Found {len(rows)} rows in HTML table")

        for row_num, row in enumerate(rows, 1):
            cells = row.find_all('td')
            if len(cells) >= 6:
                # HTML table structure: Author, Title, Journal, Year, ISSN, Classification
                author_span = cells[0].find('span')
                title_span = cells[1].find('span')
                journal_span = cells[2].find('span')
                year_span = cells[3].find('span')
                issn_span = cells[4].find('span')
                classification_span = cells[5].find('span')

                if all([author_span, title_span, journal_span, year_span, issn_span, classification_span]):
                    pub = {
                        'author': author_span.get_text().strip(),
                        'title': title_span.get_text().strip(),
                        'journal': journal_span.get_text().strip(),
                        'year': year_span.get_text().strip(),
                        'issn': issn_span.get_text().strip(),
                        'classification': classification_span.get_text().strip()
                    }
                    publications.append(pub)

    return publications

def normalize_title(title):
    """Normalize title for comparison"""
    # Remove extra spaces, convert to lowercase, remove special characters
    title = re.sub(r'\s+', ' ', title.strip().lower())
    title = re.sub(r'[^\w\s]', '', title)
    return title

def find_missing_publications(csv_pubs, html_pubs):
    """Find publications that exist in CSV but not in HTML"""

    # Create normalized title sets for comparison
    html_titles = set()
    for pub in html_pubs:
        normalized_title = normalize_title(pub['title'])
        html_titles.add(normalized_title)

    missing_publications = []

    for csv_pub in csv_pubs:
        csv_title_normalized = normalize_title(csv_pub['title'])

        if csv_title_normalized not in html_titles:
            missing_publications.append(csv_pub)

    return missing_publications

def main():
    csv_file = '/Users/shahil/amity-website/AUM/ABS/ABSResearchPublicationsNEW.csv'
    html_file = '/Users/shahil/amity-website/AUM/ABS/Research & Publication.html'

    print("Extracting publications from CSV...")
    csv_publications = extract_csv_publications(csv_file)
    print(f"Found {len(csv_publications)} publications in CSV")

    print("\nExtracting publications from HTML...")
    html_publications = extract_html_publications(html_file)
    print(f"Found {len(html_publications)} publications in HTML")

    print("\nFinding missing publications...")
    missing_pubs = find_missing_publications(csv_publications, html_publications)

    print(f"\nFound {len(missing_pubs)} publications in CSV that are missing from HTML:")
    print("=" * 80)

    for i, pub in enumerate(missing_pubs, 1):
        print(f"\n{i}. CSV Row {pub['row_number']} (Sr. No. {pub['sr_no']})")
        print(f"   Author: {pub['author']}")
        print(f"   Title: {pub['title']}")
        print(f"   Journal: {pub['journal']}")
        print(f"   Year: {pub['year']}")
        print(f"   ISSN: {pub['issn']}")
        print(f"   Classification: {pub['classification']}")
        print("-" * 80)

if __name__ == "__main__":
    main()