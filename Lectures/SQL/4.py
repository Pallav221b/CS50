import csv

counts = {}

with open("Shows.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        title = row["title"]

        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1

def f(item):
    return item[1]

for title, count in sorted(counts.items(), key = f, reverse = True):
    print(title, count, sep = " -> ")