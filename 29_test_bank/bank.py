def main():
    user = str(input("start conversation!"))
    user1 = value(user)
    user1 = int(user1)
    print(f"${user1}")
    print(type(user1))

def value(greeting):
    if greeting == "hello" or greeting == "HELLO":
        m = int(0)
        return m
    elif greeting[0] == "h" or greeting[0] == "H":
        m = int(20)
        return m
    else:
        m = int(100)
        return m
if __name__ == "__main__":
    main()