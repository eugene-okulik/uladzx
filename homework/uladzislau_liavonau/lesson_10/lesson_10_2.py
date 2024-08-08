def print_me(func):
    return lambda *args, **kwargs: [func(*args, **kwargs) for _ in range(kwargs.pop('count', 1))]


def repeat_me(count=1):
    def decorator(func):
        return lambda *args, **kwargs: [func(*args, **kwargs) for _ in range(count)]
    return decorator


@print_me
def example1(text):
    print(text)


@repeat_me(count=3)
def example2(text):
    print(text)


example1('print me', count=2)
example2('print me test2')
