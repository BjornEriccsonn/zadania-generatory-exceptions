def get_next_number():
    n = 0
    while True:
        yield n
        n += 1



if __name__ == '__main__':
    #zapis utworzy generator, żeby móc odczytywać kolejne liczby całkowite w zakresie, należy użyć metody next
    examp = (i for i in range(10))
    print(next(examp))
    print(next(examp))
    print(next(examp))


    #jeśli chcemy odczytywac w nieskonczonosc, a nie jak w przykladzie w ograniczonym zakresie, mozna napisac funkcje z uzyciem while

    infinite_num_gen = get_next_number()
    print(next(infinite_num_gen))
    print(next(infinite_num_gen))
    print(next(infinite_num_gen))
    print(next(infinite_num_gen))
    print(next(infinite_num_gen))
    print(next(infinite_num_gen))
