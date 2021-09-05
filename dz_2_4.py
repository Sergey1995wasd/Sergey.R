prices = [57.08, 46.51, 97 ,51, 1,76, 22, 213, 21.44, 1.1234, 214, 3123.2231, 3123.4, 6435.32, 424.4]
print(f'\n\n{"*" * 35} A\n')
for i in prices:
    r, kk = int(i // 1), int(f'{i % 1:.02f}'[2:])
    print(f'{r} руб {kk:02d} коп,', end=' ')


print(f"\n\n{'*' * 35} B\n")
print(f"ID base: {id(prices)} - {prices}")
prices.sort()
print(f"ID change: {id(prices)} - {prices}")


print(f"\n{'*' * 35} C,D\n")
n_list = sorted(prices,reverse=True)
print(f"ID change: {id(n_list)} - {n_list}\n{n_list[:5][::-1]}")