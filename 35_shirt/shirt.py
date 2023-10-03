from PIL import Image , ImageOps
import sys
import os
arguments = sys.argv


if len(arguments) == 3:
    extensions = [".jpg" , ".jpeg", ".png"]
    extension1 = os.path.splitext(sys.argv[1])
    extension2 = os.path.splitext(sys.argv[2])
    if extension1[1] == extension2[1] and extension1[1] in extensions:
        try:
            user_image = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("file not exists")

        shirt = Image.open("shirt.png")
        size = shirt.size
        user_image = ImageOps.fit(user_image, size)
        user_image.paste(shirt , shirt)
        user_image.save(arguments[2])
    elif extension1[1] != extension2[1]:
        sys.exit("input and output have different extensions")
    else:
        sys.exit("wrong extension")
elif len(arguments) > 3:
    sys.exit("Too many command-line argiments")
elif len(arguments) < 3:
    sys.exit("Too many command-line argiments")