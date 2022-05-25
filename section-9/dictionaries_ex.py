stuff = {"Queen": "Bohemian Rhapsody", 
         "Bee Gees": "Stayin' Alive", 
         "U2": "One", 
         "Michael Jackson": "Billie Jean", 
         "The Beatles": "Hey Jude", 
         "Bob Dylan": "Like A Rolling Stone"}

print(len(stuff))

for key in stuff.keys():
    print(key)

print(stuff.values())

for item in stuff.items():
    print(item)


print(stuff.get("Promise of the Real", "Promise of the Real is not in the dictionary \'stuff\'."))