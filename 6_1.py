from lib2to3.pgen2.grammar import line

with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    for i in  content:
        print(i)

