def camel_to_snake(camel_case):
    snake_case = ""
    for i, c in enumerate(camel_case):
        if c.isupper() and i > 0:
            snake_case += "_"
        snake_case += c.lower()
    return snake_case

def main():
    user = input("camelCase:")
    user = camel_to_snake(user)
    print(user)

main()