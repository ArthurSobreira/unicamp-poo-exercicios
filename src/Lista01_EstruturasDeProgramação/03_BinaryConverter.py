def input_number(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mInvalid Number, Try Again!\033[m')
            continue
        else:
            return number


def main():
    number = input_number('Enter a number to see your binary conversion: ')
    print(f'The binary conversion of the number {number} is: {bin(number)}.')


if __name__ == '__main__':
    main()
