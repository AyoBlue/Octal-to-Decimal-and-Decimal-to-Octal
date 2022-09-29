num = input('Provide a number for the equation: ')
if not num.isnumeric():
    print(num, ' is not a number.')
else:
    num = int(num)
    option = input('Choose an input, otd/dto: ')
    if option.lower() == 'otd':
        obj = str(num)
        end = 0
        for i in range(0, len(obj)):
            if obj[i].isnumeric():
                var = int(obj[i])
                power = len(obj) - (i + 1)
                check = 8 ** power
                end = end + (var * check)

        print(end)
    elif option.lower() == 'dto':
        numbers = []
        while True:
            if (num // 8) > 0:
                numbers.append(num % 8)
                num = num // 8
            else:
                numbers.append(num % 8)
                break

        numbers.reverse()
        print(''.join([str(x) for x in numbers]))
    else:
        print(option, ' is not a valid input.')
