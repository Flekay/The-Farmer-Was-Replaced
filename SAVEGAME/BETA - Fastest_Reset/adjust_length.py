def adjust_length(number, length):
    string = str(number, 0)
    while len(string) < length:
        string = ' ' + string
    return string
    