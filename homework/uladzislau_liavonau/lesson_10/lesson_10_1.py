def print_text(func):
    def wrapper():
        func()
        print('Finished')
    return wrapper


@print_text
def my_function():
    print('Test function')


my_function()
