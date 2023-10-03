
def main():
    fruits = {}  # Use a dictionary to store fruits and their counts
    while True:
        try:
            user = input("")
            if user == "":  # Empty input, continue asking for input
                continue
            fruits[user.lower()] = fruits.get(user.lower(), 0) + 1  # Increment the count of the fruit
        except EOFError:
            break

    sorted_fruits = sorted(fruits.items())

    for fruit, count in sorted_fruits:
        print(f"{count} {fruit.upper()}")


if __name__ == "__main__":
    main()
