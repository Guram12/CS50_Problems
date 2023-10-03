month = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

while True:
    try:
        user = input("Date: ")
        if "/" in user:
            mm, dd, yyyy = user.split("/")
            if mm[0].isalpha():
                continue
            mm = int(mm)
            if mm in range(1, 13) and int(dd) in range(1, 32):
                dd = int(dd)
                yyyy = int(yyyy)
                print(f"{yyyy}-{mm:02d}-{dd:02d}")
                break

        elif "," in user:
            mm_dd, yyyy = user.split(",")
            mm, dd = mm_dd.split(" ")
            yyyy = yyyy.replace(" ","")
            if mm_dd[0].isdigit() and "/" in user:
                continue
            elif int(dd) not in range(1,32):
                continue
            elif mm in month:
                mm = month.index(mm) + 1
                dd = int(dd)
                yyyy = int(yyyy)
                print(f"{yyyy}-{mm:02d}-{dd:02d}")
                break
    except ValueError:
        continue
