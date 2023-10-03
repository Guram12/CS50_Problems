import sys
arguments = sys.argv

def main():
    if len(arguments) == 2 and arguments[1][-2:] == "py":
        try:
            num_lines = file_reader(arguments[1])
            print(num_lines)
        except FileNotFoundError:
            sys.exit("File does not exists")
    elif arguments[1][-2:] != "py":
        sys.exit("Not a python file")
    elif len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    elif len(arguments) < 2:
        sys.exit("Too mfew command-line arguments")

def file_reader(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        num_lines = 0
        for line in lines:
            line1 = line.strip()
            if line1 and not line1.startswith("#") or not line1.startswith(""):
                num_lines += 1
        return str(num_lines)


if __name__ == "__main__":
    main()
