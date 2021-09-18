import re

s = input("Do You Agree?\n")

if re.search("^y(es)?$", s.lower()):
    print("Agreed.")
elif re.search("^n(o)?$", s.lower()):
    print("Not Agreed.")
else:
    print("Wrong Input")
