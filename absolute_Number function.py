def get_absolute(number):

    """
    if you pass a positive number return it as a same number
    but if you pass a negative number return it as a negative number, -number
    is returned
    """
    if number >= 0:
        return number
    else:
        return -number

print(get_absolute(-2))
print(get_absolute(2))

