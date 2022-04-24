cel = int(input("Enter the integer representing the celsius temperature. "))


def faren(c):
    return round((1.8 * c + 32), 1)


print("The Fahrenheit equivalent of " + str(cel) + " degrees Celsius is " + str(faren(cel)) + ".")