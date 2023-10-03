import inflect
p = inflect.engine()
my_list = []
while True:
    try:
        user = input("")
        words = user.split()
        joined_words = p.join(words)
        my_list.append(joined_words)
    except EOFError:
        result = p.join(my_list)
        print(f"Adieu, adieu, to {result}")
        break
