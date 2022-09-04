"""
Simple FizzBuzz game, which requests a user to enter a number and checks it divisibility
If the number is divided by three without modulus, the program prints 'Fizz';
if the number is divided by five without modulus, the program prints 'Buzz';
if the number is divided by three and five without modulus, the program prints 'FizzBuzz'.
In the other case, it prints the number
"""


def FizzBuzz1():
    """
    The function has the range set from 1 to 100,
    therefore, it checks all these numbers and prints results
    """
    for number in range(1, 100 + 1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
            continue
        elif number % 3 == 0:
            print('Fizz')
            continue
        elif number % 5 == 0:
            print('Buzz')
            continue
        else:
            print(number)
    print('---------------------------------------------')


def FizzBuzz2(numbero):
    """
    The function takes the checked number while being called,
    it checks FizzBuzzibility and prints the result
    """
    if type(numbero) != int:
        print('Wrong type of data')
    elif numbero % 3 == 0 and numbero % 5 == 0:
        print('FizzBuzz')
    elif numbero % 3 == 0:
        print('Fizz')
    elif numbero % 5 == 0:
        print('Buzz')
    else:
        print(numbero)

