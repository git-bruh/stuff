def spam(word):
    limit = 2000
    length = int((limit // len(word)))
    output = word * length
    return output
