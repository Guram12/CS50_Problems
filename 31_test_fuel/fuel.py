def main():
    while True:
        user = input("Fraction: ")
        result1 = convert(user)
        result2 = gauge(result1)
        if result2 is not None:
            print(result2)
            break

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        result = x / y
        result = float(result)
        return round(result * 100)
    except ValueError:
        raise ValueError("Invalid fraction format")
    except ZeroDivisionError:
        raise ZeroDivisionError("devision by zero")

def gauge(percentage):
    if 0 <= percentage < 10:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif 10 <= percentage < 99 :
         res = round(percentage)
         return str(f"{res}%")
    else:
        return None


if __name__ == "__main__":
    main()






















