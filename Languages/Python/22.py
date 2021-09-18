d = {
    1 : "Mon",
    2 : "Tues",
    3 : "Wed",
    4 : "Thurs",
    5 : "Fri",
    6 : "Sat",
    7 : "Sun"
}

print(d[3])
print(d.get(3))
print(d.get(8))
print(d.get(8, "Not cool man"))
