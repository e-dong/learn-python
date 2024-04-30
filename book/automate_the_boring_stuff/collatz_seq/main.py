def collatz(number: int):
    """Calculates the next collatz sequence given an integer"""
    if number % 2 == 0:
        val = number // 2 
    else:
        val = 3 * number + 1
    
    print(val)
    return val

def main():
    # Input validation loop
    input_int = None
    while input_int is None or input_int < 1:
        try:
            print("Enter an integer greater than 0:")
            input_int = int(input())
            if input_int < 1:
                raise ValueError(f"Input int [{input_int}] is less than 1")
        except ValueError as e:
            print(f"Error inputed value is not an int greater than 0: {e}")

    result_int = collatz(input_int) 
    while result_int != 1:
        result_int = collatz(result_int)

if __name__ == "__main__":
    main()

