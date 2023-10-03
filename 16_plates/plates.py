def main():
    user = input("Plate: ")
    user = user.upper()
    if is_valid1(user) :
        print("Valid")
    else:
        print("Invalid")

def is_valid1(s):
    if len(s) < 2 or len(s) > 6:
        return False

    for l in s[:2]:
        if not l.isalpha():
            return False

    for i in s:
        if i.isdigit():
            index = s.index(i)
            if not s[index:].isdigit():
                return False

    i = 0
    while i < len(s):
        if s[i].isdigit() == True:
            if s[i] == "0":
                return False
            break
        i += 1

    for i in s:
        if i.isdigit():
            if i == '0':
                return False
            return True


    if s[0].isdigit():
        return False


    for i in s:
        if i in [".", ",", "!", "?", " ", ]:
            return False
        return True



main()