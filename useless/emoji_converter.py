def emoji_converter(message):
    words = message.split(' ')
    emoji_mapping = {
        ':)':  '😃',
        ':(': '😟',
        ':*': '😘',
        ":'(": '😢',
        ":/": '😕',
        "/shrug": '¯\_(ツ)_/¯'
    }
    output = ''
    for word in words:
        output += emoji_mapping.get(word, word) + ' '
    return output


output = emoji_converter(input("> "))
