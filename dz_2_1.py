# 1. Выяснить тип результата выражений:
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a),type(b),type(c),type(d))

list_1 = (15 * 3, 15 / 3, 15 // 2, 15 ** 2)
for i in list_1:
    print(type(i))