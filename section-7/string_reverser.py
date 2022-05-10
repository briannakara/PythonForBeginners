words = input("Say anything! ")
reverse = ""

for num in range(1, len(words)+ 1, 1):
    num = num * -1
    reverse += words[num]
print(reverse)

