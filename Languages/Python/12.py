a = [1, 2, 3]
b = ['a', 'b', 'c']

a.extend(b)
print(a)
print(b)

b.append('d')
print(b)

a.insert(0, 50)
print(a)

a.remove("c")
print(a)

a.clear()
print(a)

b.pop()
print(b)
