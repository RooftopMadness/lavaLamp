import roundArray

ra = roundArray.RoundArray(5, 7)
ra.set(4, 6, 7.5)

print(ra.get(4, 6))
print(ra.get(9, 6))
print(ra.getArr())


