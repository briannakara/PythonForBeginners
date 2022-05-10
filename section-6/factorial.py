number = int(input("Enter an integer: "))


def factorial(num):
    product = 1
    while num > 0:
        product *= num
        num -= 1
    return product


print(number)
print(factorial(number))