import csv

title = input("Title : ")

with open("data.tsv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        if title == row["primaryTitle"]:
            print(row["primaryTitle"], row["startYear"])
