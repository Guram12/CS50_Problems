

def main():
    while True:
        user = input("Fraction: ")
        try:
            result = results(user)
            if result is not None:
                print(result)
                break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def convert(user):
    a, b = user.split("/")
    a = int(a)
    b = int(b)
    result = a / b
    result = float(result)
    return result

def results(r):
    res = convert(r)
    if 0 <= res < 0.1:
        return "E"
    elif 0.99 <= res <= 1:
        return "F"
    elif 0.1 <= res < 0.99 :
        return f"{round(res * 100)}% "
    return None


if __name__ == "__main__":
    main()