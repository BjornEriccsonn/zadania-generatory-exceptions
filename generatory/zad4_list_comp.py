
if __name__ == '__main__':
    numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]
    filtered_number = [numbers[i] for i in range(len(numbers)) if numbers[i] <= 0]
    print(filtered_number)