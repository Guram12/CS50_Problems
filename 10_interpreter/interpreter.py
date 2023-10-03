math_nums = input("Enter a math expression: ")
x, y, z = math_nums.split(" ")

if y == "+":
    result = float(x) + float(z)
    f_result = "{:.1f}".format(result)
    print(f_result)
elif y == "-":
    result = float(x) - float(z)
    f_result = "{:.1f}".format(result)
    print(f_result)
elif y == "/":
    result = float(x) / float(z)
    f_result = "{:.1f}".format(result)
    print(f_result)
elif y == "*":
    result = float(x) * float(z)
    f_result = "{:.1f}".format(result)
    print(f_result)