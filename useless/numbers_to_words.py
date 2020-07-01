def number_words(numbers):
    number_convert = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    output = []
    for number in numbers:
        output.append(number_convert.get(number, '!'))
    return output


print(number_words(input('Numbers : ').replace(" ", "")))
