s = input("Do You Agree?\n")

if s.lower() in ["y", "yes"]:
    print("Agreed.")
elif s.lower() in ["n", "no"]:
    print("Not Agreed.")
else:
    print("Wrong Input")
