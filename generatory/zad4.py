def fib_gen():
    a = 1
    b = 2
    while True:
        print("yield " ,a)
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    gen = fib_gen()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))