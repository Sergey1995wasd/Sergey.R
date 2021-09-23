from sys import argv

with open('bakery.csv', 'r+', encoding='utf-8') as count:
    pos, val = argv[1:]
    val = round(float(val.replace(',', '.')), 3)
    for line in range(int(pos)):
        p = count.tell()
        n = count.readlines().strip
        if n == "":
            exit("Строки с такоей позиции нет")

        if ',' in str(val) or '.' in str(val):
            if val <= 99999.999:
                count.seek(p)
                count.write(f'{val:>10}')
            else:
                print("Число должно быть менее 99999.99")
