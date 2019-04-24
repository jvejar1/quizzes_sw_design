def add(numbers_str, delimiter = None):
    if delimiter:
        numbers = numbers_str.split(delimiter)
    else:
        numbers = numbers_str.split(',')
    numbers = [int(number) for number in numbers]
    sum = 0
    for number in numbers:
        if number>0:
            sum +=number
    return sum