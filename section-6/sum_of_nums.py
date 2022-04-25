num = int(input("Enter a positive integer: "))
initial = num
add = 0

while num > 0:
    add += num
    num -= 1

print(num)
print(add)