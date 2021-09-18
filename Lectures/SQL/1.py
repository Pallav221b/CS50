import csv

with open("Shows.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["title"])
