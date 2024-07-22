words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def values_output(**kwargs):
    for key, value in kwargs.items():
        print(key * value)


values_output(**words)
