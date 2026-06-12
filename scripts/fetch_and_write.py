import csv
from datetime import datetime
import os

import requests


def fetch_posts(limit=5):
    """Fetch sample posts from jsonplaceholder.typicode.com."""
    url = "https://jsonplaceholder.typicode.com/posts"
    resp = requests.get(url, params={"_limit": limit}, timeout=10)
    resp.raise_for_status()
    return resp.json()


def write_posts_csv(posts, filename=None):
    """Write list of post dicts to a CSV file and return the filename."""
    if filename is None:
        filename = f"posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    fieldnames = ["id", "userId", "title", "body"]
    with open(filename, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for p in posts:
            writer.writerow({k: p.get(k, "") for k in fieldnames})

    print(f"Wrote {len(posts)} posts to {filename}")
    return filename


def main(limit=5):
    posts = fetch_posts(limit=limit)
    return write_posts_csv(posts)


if __name__ == "__main__":
    # Allow simple CLI usage: python scripts/fetch_and_write.py
    try:
        output = main()
    except Exception as e:
        print("Error:", e)
        raise