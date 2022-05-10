from random import randint

gallons = randint(10, 25)
miles = randint(200, 400)


def mpg(m, g):
    return m // g


print("Your car holds " + str(gallons) + " gallons of fuel.")
print("Your car can drive " + str(miles) + " miles on a full tank without a refuel.")
print("Your car's miles per gallon is " + str(mpg(miles, gallons)) + ".")