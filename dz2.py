def recur(numb, even=0, odd=0):
    if numb == 0:
        return even, odd
    else:
        cur_n = numb % 10
        numb = numb // 10
        if cur_n % 2 == 0:
            even += 1
        else:
            odd += 1
        return recur(numb, even, odd)

try:
        numb = int(input("Введите число: "))
        print(f" Кол-во четных и нечетных цифр в числе: {recur(numb)}")
except ValueError:
        print("Неверный ввод")