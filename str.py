def str(number, round_to = 4, forced = True):
    negative = False
    if number <= 0:
        if number == 0:
            return "0"
        number = abs(number)
        negative = True
    string = ""
    n = "0123456789"
    number = (number * (10**round_to) + 0.5)
    number //= 1
    if round_to > 0 and forced == True:
        for i in range(round_to):
            string = n[number %10] + string
            number //= 10
        string = "."+string
    else:
        for i in range(round_to):
            if len(string) > 0 or number %10//1 != 0:
                string = n[number %10] + string  
            number //= 10
        if len(string) != 0:
            string = "."+string
    while number > 0:        
        string = n[number% 10] + string
        number //= 10
    if string[0] != ".":
        if negative:
            return "-" + string
        return string
    if negative:
            return "-0" + string
    return  "0" + string