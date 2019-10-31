print('Press 1 to transform binary to decimal')
print('Press 2 to transform decimal to binary')
x = input('Choose your option: ')
if x == '1':
    binary = input('Enter a number in binary form:  ')
    decimal = int(binary, 2)
    print(binary, 'In decimal=', decimal)
if x == '2':
    number = int(input('Enter your number: '))
    binary = []
    while number != 0:
        if number % 2 == 0:
            number = number / 2
            binary.insert(0, 0 )
        else:
            if number % 2 == 1:
                number = (number - 1) / 2
                binary.insert(0, 1 )
    print(binary)
