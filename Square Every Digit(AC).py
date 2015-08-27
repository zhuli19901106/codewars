def square_digits(num):
    num = map(int, list(str(num)))
    num = int(''.join(map(str, map(lambda x: x ** 2, num))))
    return num
    