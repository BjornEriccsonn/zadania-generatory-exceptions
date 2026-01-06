def primes():
    n = 2
    while True:
        is_prime = True

        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            yield n
        n += 1

if __name__ == '__main__':
   primes_gen = primes()
   val1 = next(primes_gen)
   print(val1)
   val2 = next(primes_gen)
   print(val2)
   val3 = next(primes_gen)
   print(val3)
   #val4 = next(primes_gen)
   #val5 = next(primes_gen)


