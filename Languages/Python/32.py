file = open("e.txt", "r")

print(file.readable())
for e in file.readlines():
    print(e)
    
file.close()
