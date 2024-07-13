def truncate(number, decimals=0):
    return number - (number % (1 / 10 ** decimals))
