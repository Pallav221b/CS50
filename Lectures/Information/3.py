from time import sleep

with open("Lyrics.txt", "r") as file:
    for word in file.readlines():
        print(f"Checking {word.rstrip()}...")
        sleep(.01)
