length = int(input("Enter the length of the rectangular prism. "))
width = int(input("Enter the width of the rectangular prism. "))
height = int(input("Enter the height of the rectangular prism. "))


def volume(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is " + str(volume(length, width, height)) + " cubic feet.")