class NegativeNumberError(Exception):
    pass

class NonNumericValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Non-numeric value at index {self.value} or {self.value+1}"
    pass

def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Please enter a number")

def example1():
    x = get_number( "enter a number" )
    y = get_number( "enter another number" )
    try:
        res = x/y
    except ZeroDivisionError:
        print("division by zero is forbidden")
    else:
        print( x, '/', y, '=', res )

def example2(L):
    print("\n--- Example 2 ---")
    sumOfPairs = []
    try:
        for i in range(len(L) - 1):
            if not isinstance(L[i], (int, float)) or not isinstance(L[i+1], (int, float)):
                raise NonNumericValueError(i)
            sumOfPairs.append(L[i] + L[i+1])
    except NonNumericValueError as e:
        print("Error:", e)
    else:
        print("sumOfPairs =", sumOfPairs)


def printUpperFile(fileName):
   try:
    file = open( fileName, "r" )
   except FileNotFoundError:
    print("File not found")
   except IsADirectoryError:
    print("Path is a directory")
   else:
    for line in file:
        print(line.upper())
    file.close()

    
def main():
    example1()
    L = [ 10, 3, 5, 6, 9, 3 ]
    example2( L )
    example2( [ 10, 3, 5, 6, "NA", 3 ] )
    try:
        example3( [ 10, 3, 5, 6 ] )
    except NameError:
        print("example3 is not defined")

    printUpperFile( "doesNotExistYest.txt" )
    printUpperFile( "./Dessssktop/misspelled.txt" )


if __name__ == "__main__":
    main()