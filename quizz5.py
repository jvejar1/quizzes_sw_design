def add(numbers_str, delimiter = ','):
    str_numbers = numbers_str.split(delimiter)
    sum = 0
    for str_number in str_numbers:
        number = int(str_number)
        if number > 0:
            sum += number
    return sum