def main():
    total = 0  # Initialize total to zero
    while True:
        try:
            user = input("Item: ")
            user = user.title()
            item_price = menu_list(user)
            if item_price is not None:
                tl = total + item_price
                total += item_price  # Add the item price to the total
                print(f"total: ${tl:.2f}")
            else:
                print("Item not found.")
        except EOFError:
            break
    print("Total: $" + str(round(total, 2)))  # Print the total

def menu_list(s):
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    if s in menu:
        return menu[s]  # Return the item price
    return None

main()
