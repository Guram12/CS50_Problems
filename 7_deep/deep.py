def main():
    user = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").title()
    if user == "42" :
        print("yes")
    elif "42 " in user and " " in user :
        user = user.replace(" ", "")
        print("yes")
    elif user == "Forty-Two":
        if user == str(user):
            print("yes")
    elif user == "Forty Two":
        if user == str(user):
            print("yes")
    elif user == str(user):
        print("no")
    else:
        print("no")
main()