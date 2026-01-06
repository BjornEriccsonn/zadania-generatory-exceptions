def example_gen():
    print("Start")
    yield 1
    print("After yield 1")
    yield 2
    print("After yield 2")
    yield 3
    print("Throwing exception")
    raise ValueError("EXCEPTION THROWN")


if __name__ == '__main__':
    generator = example_gen()
    first_val = next(generator)
    print(first_val)
    second_val = generator.__next__()
    print(second_val)
    third_val = next(generator)
    print(third_val)
    next(generator)
