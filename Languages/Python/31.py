try:
    k = 10/0
    n = int(input())
    print(n)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("not cool man")
