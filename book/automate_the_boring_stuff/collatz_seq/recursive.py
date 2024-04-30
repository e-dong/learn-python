import time
def collatz():
    try:
        number = int(input())
        print(number)
        while number != 1:
            if number < 0:
                print('Enter a positive integer')
                number = collatz()
            elif number % 2 == 0:
                number = number // 2
                print(number)
            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)
            time.sleep(0.01)
        return number
    except ValueError:
        print('Enter an integer')
        collatz()
print('Enter a number.')
collatz()

