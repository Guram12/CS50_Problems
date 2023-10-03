def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    tip1 = float(tip)
    print(f"Leave ${tip1:.2f}")
def dollars_to_float(dollars):
    dolar_without_sign = dollars.replace("$", "")
    return float(dolar_without_sign)
def percent_to_float(percent):
    percent_without_sign = percent.replace("%", "")
    return float(percent_without_sign) / 100
main()