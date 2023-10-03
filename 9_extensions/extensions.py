user = input("enter file name heare ->")
user = user.lower()
user = user.replace(" ", "")
if user.endswith(".gif"):
    print("image/gif")
elif user.endswith(".jpg"):
    print("image/jpeg")
elif user.endswith(".jpeg"):
    print("image/jpeg")
elif user.endswith(".png"):
    print("image/png")
elif user.endswith(".pdf"):
    print("application/pdf")
elif user.endswith(".txt"):
    print("text/plain")
elif user.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")