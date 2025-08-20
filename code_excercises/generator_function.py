def generator_function():
    """
    A generator function that yields infinite numbers.
    """
    i = 0
    while True:
        yield i
        i += 1

if __name__ == "__main__":
    gen = generator_function()
    for _ in range(10):
        print(next(gen))