words = input("Say anything! ")
words_sliced = ""

for char in words:
    if char.isalnum() or char.isspace():
        words_sliced += char

print(words_sliced.split())
print(len(words_sliced.split()))