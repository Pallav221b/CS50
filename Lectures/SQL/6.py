import csv

with open("data.tsv", "r") as titles:

    reader = csv.DictReader(titles, delimiter = "\t")

    with open("shows0.csv", "w") as shows:

        writer = csv.writer(shows)

        writer.writerow(["tconst", "primaryTitle", "startYear", "genres"])

        for row in reader:

            if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

                write.writerow([row["tconst"], row["primaryTitle"], row["startYear"], row["genres"]])
