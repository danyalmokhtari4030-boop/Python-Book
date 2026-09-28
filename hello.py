import requests
import csv

url = "https://openlibrary.org/search.json"

params = {
    "q": "python",
    "limit": 100
}

response = requests.get(url, params=params)

data = response.json()

books = []

for book in data["docs"]:
    year = book.get("first_publish_year")

    if year and year > 2000:
        title = book.get("title", "Unknown")

        authors = ", ".join(
            book.get("author_name", ["Unknown"])
        )

        books.append({
            "title": title,
            "author": authors,
            "year": year
        })

        if len(books) == 50:
            break

with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["title", "author", "year"]
    )

    writer.writeheader()
    writer.writerows(books)

print(f"{len(books)} books saved to books.csv")