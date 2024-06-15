# ## Function: str

# ### Description:
# This function converts a number into a string representation with a specified number of decimal places. If the number is negative, it is converted to its absolute value before the conversion. The function also has an option to force the number of decimal places.

# ### Parameters:
# - `number` (float or int): The number to be converted to a string.
# - `precision` (int, optional): The number of decimal places to round the number to. Default is 4.

# ### Returns:
# - `string` (str): The string representation of the number with the specified number of decimal places.

# ### Example:
# ```python
# quick_print(str(123.4567826984))
# # Output: "123.4567"


def str(number, precision = 4):
    negative = False
    if number <= 0:
        if number == 0:
            return "0"
        number = abs(number)
        negative = True
    string = ""
    n = "0123456789"
    number = (number * (10**precision) + 0.5)
    number //= 1
    for i in range(precision):
        string = n[number %10] + string
        number //= 10
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