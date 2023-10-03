total_cost = 50

while True:
    print("Amount Due:", total_cost)
    user_input = int(input("Insert Coin: "))

    if user_input in [5, 10, 25]:
        total_cost -= user_input

        if total_cost > 0:
            print("Amount Due:", total_cost)
        else:
            break
    else:
        continue

print("Change Owed:", -total_cost)
