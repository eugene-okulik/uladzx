def fibonacci():
    fib1, fib2 = 0, 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


def get_fibonacci_number(position):
    fib_gen = fibonacci()
    fib_number = 0
    for i in range(position):
        fib_number = next(fib_gen)
    return fib_number


print("Пятое число Фибоначчи:", get_fibonacci_number(5))
print("Двухсотое число Фибоначчи:", get_fibonacci_number(200))
print("Тысячное число Фибоначчи:", get_fibonacci_number(1000))
print("Стотысячное число Фибоначчи:", get_fibonacci_number(100000))
