
def main():
    user = str(input("Input: "))
    user1 = shorten(user)
    print("output:", user1)



def shorten(x):
    vowels = "aeiouAEIOU"
    result = ""
    for char in x:
        if char not in vowels:
            result += char

    return result

if __name__ == "__main__":
    main()