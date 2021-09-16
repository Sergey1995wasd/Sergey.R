from itertools import islice, zip_longest
names = ['Sasha', 'Masha', 'Pasha', 'Dasha']
classes = ['11b', '11a', '7a']

gen = (i for i in zip_longest(names, classes) if len(names) > len(classes))

print(*islice(gen, 9))
print(*islice(gen, 3))