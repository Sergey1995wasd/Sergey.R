from functools import wraps


def type_loggeer (func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        num_list = [el for el in (*args, *kwargs.value())]
        n = [f"{func.__name__}({el}: {type(el)})" for el in num_list]
        print(*n, *func(*args, **kwargs), sep=",\n")

    return wrapper


@type_loggeer
def cal_cube(*x, **y):
    num_list = [el for el in (*x,*y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for  i in num_list]


a = cal_cube(1, {'num': 3}, (2, 'name'), {2,15}, [1,8])

print(cal_cube.__name__)
help(cal_cube)