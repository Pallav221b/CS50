from sys import argv, exit

if len(argv) != 2:
    print("missing cmd-ling-arg")
    exit(1)
print(f"hello, {argv[1]}")
exit(0)
