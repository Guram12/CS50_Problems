from emoji import emojize as em

def main():
    user = input("Input: ")
    user = convert(user)
    print(user)



def convert(e):
    txt = em(e)
    return txt



if __name__ == "__main__":
    main()


